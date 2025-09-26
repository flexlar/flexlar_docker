import os
import re


def get_versions():
    flexlar_version = os.getenv("FLEXLAR_VERSION")
    erpnext_version = os.getenv("ERPNEXT_VERSION")
    assert flexlar_version, "No Flexlar version set"
    assert erpnext_version, "No ERPNext version set"
    return flexlar_version, erpnext_version


def update_pwd(flexlar_version: str, erpnext_version: str):
    with open("pwd.yml", "r+") as f:
        content = f.read()
        content = re.sub(
            rf"flexlar/erpnext:.*", f"flexlar/erpnext:{erpnext_version}", content
        )
        f.seek(0)
        f.truncate()
        f.write(content)


def main() -> int:
    update_pwd(*get_versions())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
