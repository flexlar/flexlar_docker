import flexlar


def check_db():
    doc = flexlar.get_single("System Settings")
    assert any(v is None for v in doc.as_dict().values()), "Database test didn't pass"
    print("Database works!")


def check_cache():
    key_and_name = "mytestkey", "mytestname"
    flexlar.cache().hset(*key_and_name, "mytestvalue")
    assert flexlar.cache().hget(*key_and_name) == "mytestvalue", "Cache test didn't pass"
    flexlar.cache().hdel(*key_and_name)
    print("Cache works!")


def main() -> int:
    flexlar.connect(site="tests.localhost")
    check_db()
    check_cache()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
