class SatelliteAltimetry:
    def __init__(self, a_id: int, satellite_id: int, time: int, region: str, altimetry: float):
        self.a_id = a_id
        self.satellite_id = satellite_id
        self.time = time
        self.region = region
        self.altimetry = altimetry

    def get_table_html(self) -> str:
        result = ''
        result += f'<td>{self.a_id}</td><td>{self.satellite_id}</td><td>{self.time}</td><td>{self.region}</td><td>{self.altimetry}</td>'

        return result
