import settings

try:
    res = settings.lol_watcher.match.timeline_by_match(region=settings.platform, match_id='JP1_477183227')
    print(res)
except settings.ApiError as err:
    if err.response.status_code == 404:
        print('Active game not found.')
    else:
        raise