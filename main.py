import requests

url_1 = 'https://www.google.com/search?q=pycharm+community+install&rlz=1C1GCEB_enUA874UA874&ei=1_KYYd2NG-WlrgSFyK34Ag&oq=pycharm+community+in&gs_lcp=Cgdnd3Mtd2l6EAMYADI' \
        'FCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEB' \
        'YQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOhAILhDHARDRAxDIAxCwAxBDOgQIABBDSgUIOBIBMUoECEEYAFCgA1jFHGCDKmgDcAJ4AIABkwGIAeAEkgEDMC41mAEAoAEByAEMwAEB&sclient=gws-wiz'

url_2 = 'https://www.python.org/dev/peps/pep-0008/'
domain = 'www.python.org'
path = '/authenticated'


def parse_parameters(query: str) -> dict:
    list_link = query.split(sep="?")
    dict_parameters = {}

    if len(list_link)>1:
        list_parameters = [i.split(sep="=") for i in list_link[1].split(sep="&")]
        for i in range(len(list_parameters)):
            dict_parameters.update({list_parameters[i][0]: list_parameters[i][1]})

    return dict_parameters


def parse_cookies(query: str) -> dict:
    dict_cookies = {}
    r= requests.get(url_2, query)
    r.cookies.get_dict()

    return dict_cookies


if __name__ == '__main__':
    # # Tests for function "parse_parameters"
    assert parse_parameters(url_1) == {}
    assert parse_parameters(url_1) == {'name': 'ferret',
                                      'color': 'purple'}
    # assert
    # assert
    # assert

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies({'1P_JAR': '2021-11-20-16'}) == {'1P_JAR': '2021-11-20-16'}
    assert parse_cookies({'location ': 'New York'}) == {'location ': 'New York'}
    assert parse_cookies({'cartId ': ''}) == {}



# requestsJar = requests.cookies.RequestsCookieJar()
# requestsJar.set("name","Dima", domain= domain, path=path)
# dict_cookies = requests.get(url_2)