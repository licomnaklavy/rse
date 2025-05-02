class SatelliteImage:
    def __init__(self, s_id: int, image_path: str, time: int, description: str, satellite_id: int):
        self.s_id: int = s_id
        self.image_path: str = image_path
        self.time: int = time
        self.description: str = description
        self.satellite_id: int = satellite_id

