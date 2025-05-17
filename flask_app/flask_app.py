from flask import Flask, render_template
from db.database import Database


class Flask_app:
    def __init__(self):
        self.app = Flask(__name__)
        self.create_routing()
        self.database = Database()

    def create_routing(self):
        @self.app.route("/")
        def show_main_page():
            return render_template('rse_main.html')

        @self.app.route("/raw_data")
        def show_raw_data():
            return render_template('raw_data.html')

        @self.app.route("/satellite_images")
        def show_satellite_images():
            path_to_dir = 'https://storage.yandexcloud.net/practicaphotos/'

            paths_to_images = []

            for satellite_image in self.database.get_satellite_images():
                paths_to_images.append(satellite_image.image_path)

            result_path = ''
            for i in paths_to_images:
                result_path += f'<img class="imgbox center-fit" src="{path_to_dir + i}" alt="{i}">'

            return render_template('satellite_images.html', img_list=result_path)

        @self.app.route("/radar_images")
        def show_radar_images():
            path_to_dir = 'https://storage.yandexcloud.net/practicaphotos/'

            paths_to_images = []

            for radar_image in self.database.get_radar_images():
                paths_to_images.append(radar_image.image_path)

            result_path = ''
            for i in paths_to_images:
                result_path += f'<img class="imgbox center-fit" src="{path_to_dir + i}" alt="{i}">'

            return render_template('radar_images.html', img_list=result_path)

        @self.app.route("/satellite_altimetry")
        def show_satellite_altimetry():
            altimetry_data = []

            for altimetry in self.database.get_satellite_altimetry():
                altimetry_data.append(altimetry)

            result_path = ''

            for row in altimetry_data:
                result_path += '<tr>'
                result_path += row.get_table_html()
                result_path += '</tr>'

            return render_template('satellite_altimetry.html', altimetry_list=result_path)

        @self.app.route("/satellite_gravimetry")
        def show_satellite_gravimetry():
            gravimetry_data = []

            for gravimetry in self.database.get_satellite_gravimetry():
                gravimetry_data.append(gravimetry)

            result_path = ''

            for row in gravimetry_data:
                result_path += '<tr>'
                result_path += row.get_table_html()
                result_path += '</tr>'

            return render_template('satellite_gravimetry.html', gravimetry_list=result_path)

        @self.app.route("/satellite_magnetometry")
        def show_satellite_magnetometry():
            magnetometry_data = []

            for magnetometry in self.database.get_satellite_magnetometry():
                magnetometry_data.append(magnetometry)

            result_path = ''

            for row in magnetometry_data:
                result_path += '<tr>'
                result_path += row.get_table_html()
                result_path += '</tr>'

            return render_template('satellite_magnetometry.html', magnetometry_list=result_path)
