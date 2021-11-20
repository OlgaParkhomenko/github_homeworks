import requests

url = 'https://www.google.com/search?q=pycharm+community+install&rlz=1C1GCEB_enUA874UA874&ei=1_KYYd2NG-WlrgSFyK34Ag&oq=pycharm+community+in&gs_lcp=Cgdnd3Mtd2l6EAMYADI' \
        'FCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEB' \
        'YQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOhAILhDHARDRAxDIAxCwAxBDOgQIABBDSgUIOBIBMUoECEEYAFCgA1jFHGCDKmgDcAJ4AIABkwGIAeAEkgEDMC41mAEAoAEByAEMwAEB&sclient=gws-wiz'

url_2 = 'https://www.google.com'


def parse_parameters(query: str) -> dict:
    dict_parameters = {}
    list_link = query.split(sep="?")

    try:
        list_parameters = []
        for i in list_link[1].split(sep="&"):
            list_parameters.append(i.split(sep="="))
        for i in range(len(list_parameters)):
            dict_parameters.update({list_parameters[i][0]: list_parameters[i][1]})
    except IndexError:
        print('No parameters in URL')

    return dict_parameters


def parse_cookies(query: str) -> dict:
    cookies = {'cookies': query}
    r = requests.get(url, cookies=cookies)
    dict_cookies = dict(r.cookies.items())

    return dict_cookies


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters(url) != {}
    assert parse_parameters(url) != {'name': 'ferret', 'color': 'purple'}
    assert parse_parameters(url).get('sclient') == 'gws-wiz'
    assert list(parse_parameters(url).keys())[0] == 'q'
    assert parse_parameters(url) != {'name': 'Dima'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') != {'name': 'Dima'}
    assert parse_cookies('1P_JAR=2021-11-20-20') == {'1P_JAR': '2021-11-20-20'}
    assert parse_cookies('location=New York') == {'location ': 'New York'}
    assert parse_cookies({'cartId ': ''}) == {}