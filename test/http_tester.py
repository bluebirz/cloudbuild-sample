import os
import subprocess
import uuid

import requests
from requests.packages.urllib3.util.retry import Retry


def test_args():
    port = os.getenv(
        "PORT", 8080
    )  # Each functions framework instance needs a unique port

    # access `\src` directory
    target_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
    process = subprocess.Popen(
        [
            "functions-framework",
            "--target",
            "hello_http",
            "--port",
            str(port),
            "--debug",
        ],
        cwd=target_dir,
        stdout=subprocess.PIPE,
    )

    # Send HTTP request simulating Pub/Sub message
    # (GCF translates Pub/Sub messages to HTTP requests internally)
    BASE_URL = f"http://localhost:{port}"

    retry_policy = Retry(total=6, backoff_factor=1)
    retry_adapter = requests.adapters.HTTPAdapter(max_retries=retry_policy)

    session = requests.Session()
    session.mount(BASE_URL, retry_adapter)

    # name = str(uuid.uuid4())
    # res = session.post(BASE_URL, json={"name": name})
    # assert res.text == "Hello {}!".format(name)
    res = session.get(BASE_URL)
    print("text = ", res.text)
    assert res.text == "Hello World"

    # Stop the functions framework process
    process.kill()
    process.wait()
