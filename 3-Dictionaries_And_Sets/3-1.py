# coding: utf-8
tt = (1,2,(30,40))
hash(tt)
tl = (1,3,[30,40])
hash(tl)
tf = (1,2,frozenset([30,40]))
hash(tf)
DIAL_CODES = [
    (86,'China'),
    (91,'India'),
    (1,'United State'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country:code for code, country in DIAL_CODES}
country_code
{code: country.upper() for country, code in country_code.items() if code < 66 }
