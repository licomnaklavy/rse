class SatelliteMagnetometry:
    def __init__(self, m_id: int, satellite_id: int, time: int, region: str, magnetometry: float):
        self.m_id = m_id
        self.satellite_id = satellite_id
        self.time = time
        self.region = region
        self.magnetometry = magnetometry

    def get_table_html(self) -> str:
        result = ''
        result += f'<td>{self.m_id}</td><td>{self.satellite_id}</td><td>{self.time}</td><td>{self.region}</td><td>{self.magnetometry}</td>'

        return result
