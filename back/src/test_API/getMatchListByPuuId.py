import settings

try:
    res = settings.lol_watcher.match.matchlist_by_puuid(region=settings.platform, puuid=settings.puuid)
    print(res)
    # ['JP1_477183227', 'JP1_477179168', 'JP1_477172802', 'JP1_477169547', 'JP1_476891230', 'JP1_476881725', 'JP1_476869704', 'JP1_476860502', 'JP1_476852128', 'JP1_475684857', 'JP1_475674916', 'JP1_475664680', 'JP1_475654870', 'JP1_475557466', 'JP1_475552380', 'JP1_475543967', 'JP1_475538682', 'JP1_475526289', 'JP1_475514542', 'JP1_475506295']
except settings.ApiError as err:
    if err.response.status_code == 404:
        print('Active game not found.')
    else:
        raise