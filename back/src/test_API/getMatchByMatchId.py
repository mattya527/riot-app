import settings

try:
    res = settings.lol_watcher.match.by_id(region=settings.platform, match_id='JP1_477183227')
    print(res)
    # {'id': 'cA9GsDIF7hjXIri7LoNeqfF1RtryOah2-k4W-BIwci8sNA', 'accountId': '5UA1Ad4bCf9_OfAQBjXq7kQsKbR5ksG1Dpxk67JqBNsFBDo', 'puuid': 'QCCbUgKwomSanKMUNZQq5ui14SUmVUbFVeq6VLejUgVDFAuaOMnHbD9i2iMQzA0CFYpJyhboFRBE7g', 'profileIconId': 6696, 'revisionDate': 1730305402929, 'summonerLevel': 752}
except settings.ApiError as err:
    if err.response.status_code == 404:
        print('Active game not found.')
    else:
        raise