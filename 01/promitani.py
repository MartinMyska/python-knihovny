# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

def prevod(vstup):
    """takes in time in minutes and returns it as HH:MM"""
    movie_length_formatted = []
    for movie_length in vstup:
        whole_hours = str(movie_length // 60)
        minutes = str(movie_length % 60)
        if len(minutes) == 1:
            minutes = "0" + minutes
        movie_length_formatted.append(f"{whole_hours}:{minutes}")
    return movie_length_formatted


delky = [126, 105, 82]

print(prevod(delky))
