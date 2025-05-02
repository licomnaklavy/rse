class SatelliteGravimetry:
    def __init__(self, g_id: int, time: int, region: str, satellite_id: int, gravimetry: float):
        self.g_id = g_id
        self.satellite_id = satellite_id
        self.time = time
        self.region = region
        self.gravimetry = gravimetry

    def get_table_html(self) -> str:
        result = ''
        result += f'<td>{self.g_id}</td><td>{self.satellite_id}</td><td>{self.time}</td><td>{self.region}</td><td>{self.gravimetry}</td>'

        return result
