import psycopg2
import time 


def get_pokemons_from_db(north, south, west, east):
    conn = psycopg2.connect(host = "pokemons.cjgbhp9rmfkt.us-west-2.rds.amazonaws.com",
                            port = 5432,
                            user = "pokemons",
                            password = "123123sss",
                            database = "pokemons")
    
    with conn.cursor() as cur :
        cur.execute("SELECT expire,pokemon_id, latitude, longitude" +
                    " FROM pokemon_map " + 
                    " WHERE longitude > %s" +
                    " AND longitude < %s" +
                    " AND latitude > %s" +
                    " AND latitude < %s" +
                    " AND expire > %s" +
                    " LIMIT 100", 
                    (west, east, south, north, time.time() * 1000))
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({
                            "expire" : row[0],
                            "pokemon_id" : row[1],
                            "latitude" : row[2],
                            "longitude" : row[3]   
                            })    
    conn.commit()
    return result

if __name__ == "__main__":
    print get_pokemons_from_db(-34,34,-118.4,-118.2)    
