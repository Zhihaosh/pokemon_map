import psycopg2



def add_pokemon_to_db(encounter_id, expire, pokemon_id, latitude, longitude):
    conn = psycopg2.connect(host = "pokemons.cjgbhp9rmfkt.us-west-2.rds.amazonaws.com",
                            port = 5432,
                            user = "pokemons",
                            password = "123123sss",
                            database = "pokemons")
    with conn.cursor() as cur :
        cur.execute("INSERT INTO pokemon_map (encounter_id, expire, pokemon_id, latitude, longitude)"+
                    "VALUES(%s, %s, %s, %s, %s)"+
                    " ON CONFLICT (encounter_id) DO NOTHING", (encounter_id, expire, pokemon_id, latitude, longitude))
    conn.commit()
    print 'finish'
    return 
if __name__ == "__main__":
    add_pokemon_to_db(2,2,2,2,2)
    
