from .lib import is_dns_name, is_ip_octet, is_ip


class TestHostFiles:

    def usage(self):
        assert True

    def test_is_dns_name(self):
        assert not is_dns_name("no_good")
        assert not is_dns_name("no good")
        assert is_dns_name("goodhostname.com")
        assert is_dns_name("good-hostname.com")
        assert is_dns_name("www.good-hostname.com")
        assert is_dns_name("http://www.good-hostname.com")
        assert is_dns_name("https://www.good-hostname.com")

    def test_is_ip_octet(self):
        assert not is_ip_octet(256)
        assert not is_ip_octet(400)
        assert is_ip_octet(10)
        assert is_ip_octet(172)
        assert is_ip_octet(192)

    def test_is_ip(self):
        assert not is_ip("")
        assert not is_ip("127.0.3")
        assert not is_ip("127.0.3.300")
        assert is_ip("192.168.0.254")
        assert is_ip("192.168.0.255")

    def search_hosts(self):
        pass

    def update_host(self):
        pass


def app(capsys):
    # pylint: disable=W0612,W0613
    blueprint.Blueprint.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out

