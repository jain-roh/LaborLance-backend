from LaborLance.InitialMigrations.models import CityState
from LaborLance.InitialMigrations import city_state
def run():
    # Fetch all questions

    # Delete questions
    for item in city_state.city_state:

        d = CityState()

        for k, v in item.iteritems():
            setattr(d, k.lower(), v)

        d.save()