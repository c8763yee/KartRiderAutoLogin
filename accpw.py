import json
"""
you need to create your acc.json first
acc.jsn should looks like:

{
    <website>:{
        acc: <account>,
        pw: <password>
    }
}

"""


def fetchFrom(site):
    with open('acc.json') as file:
        f = json.load(file)

    return f[site]['acc'],f[site]['pw']
