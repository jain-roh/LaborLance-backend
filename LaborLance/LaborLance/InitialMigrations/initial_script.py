from LaborLance.InitialMigrations.models import CityState,Skill
from LaborLance.InitialMigrations import city_state,skills
def run():
    # Fetch all questions

    # Delete questions
    for item in city_state.city_state:

        d = CityState()

        for k, v in item.iteritems():
            setattr(d, k.lower(), v)
        d.save()

    for skill in skills.skill:
        s=Skill()
        setattr(s,'skill',skill)
        s.save()