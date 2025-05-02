import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from db.radar_image import RadarImage
from db.satellite_altimetry import SatelliteAltimetry
from db.satellite_gravimetry import SatelliteGravimetry
from db.satellite_image import SatelliteImage
from db.satellite_magnetometry import SatelliteMagnetometry


class Database:
    def __init__(self):
        self.connection = (psycopg2.connect(
            user=os.getenv("postgres_user"),
            password=os.getenv("postgres_password"),
            host=os.getenv("postgres_host"),
            port=os.getenv("postgres_port"),
            database="rse_db"
        ))

        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

    # Общая информация по спутникам
    def get_all_satellites(self):
        self.cursor.execute('''
        SELECT * FROM satellite
        ''')
        result = self.cursor.fetchall()
        return result

    # Визуальная информация
    def get_satellite_images(self) -> list[SatelliteImage]:
        self.cursor.execute(f'''
                SELECT * FROM satellite_images ORDER BY id
                ''')
        result = self.cursor.fetchall()
        satellite_images_list: list[SatelliteImage] = []
        for i in result:
            satellite_images_list.append(SatelliteImage(*i))
        return satellite_images_list

    def get_radar_images(self) -> list[RadarImage]:
        self.cursor.execute(f'''
                SELECT * FROM radar_images ORDER BY id
                ''')
        result = self.cursor.fetchall()
        radar_images_list: list[RadarImage] = []
        for i in result:
            radar_images_list.append(RadarImage(*i))
        return radar_images_list

    # Числовые данные
    def get_satellite_altimetry(self) -> list[SatelliteAltimetry]:
        self.cursor.execute(f'''
                SELECT * FROM satellite_altimetry
                ''')
        result = self.cursor.fetchall()
        altimetry_list: list[SatelliteAltimetry] = []
        for i in result:
            altimetry_list.append(SatelliteAltimetry(*i))
        return altimetry_list

    def get_satellite_gravimetry(self) -> list[SatelliteGravimetry]:
        self.cursor.execute(f'''
                SELECT * FROM satellite_gravimetry
                ''')
        result = self.cursor.fetchall()
        gravimetry_list: list[SatelliteGravimetry] = []
        for i in result:
            gravimetry_list.append(SatelliteGravimetry(*i))
        return gravimetry_list

    def get_satellite_magnetometry(self) -> list[SatelliteMagnetometry]:
        self.cursor.execute(f'''
                SELECT * FROM satellite_magnetometry
                ''')
        result = self.cursor.fetchall()
        magnetometry_list: list[SatelliteMagnetometry] = []
        for i in result:
            magnetometry_list.append(SatelliteMagnetometry(*i))
        return magnetometry_list
