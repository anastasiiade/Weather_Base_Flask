from db_connection.connection import BaseDBView, fdb


class Weather(BaseDBView):
    def get_all(self):
        self.connector.cursor.execute('''
                                        select 
                                        weather.id,
                                        weather.forecast_date,
                                        weather.avg_temp,
                                        weather.avg_pressure,
                                        weather.avg_rainfall,
                                        weather.id_city,
                                        weather_cities.name_city
                                    from weather
                                       inner join weather_cities on (weather.id_city = weather_cities.id)
                                    ''')
        result = self.connector.cursor.fetchallmap()
        self.connector.cursor.close()
        return result

    def get_by_id(self, w_id):
        self.connector.cursor.execute('''
                                        select
                                        weather.id,
                                        weather.id_city,
                                        weather.forecast_date,
                                        weather.avg_temp,
                                        weather.avg_pressure,
                                        weather.avg_rainfall,
                                        weather_cities.name_city
                                    from weather
                                       inner join weather_cities on (weather.id_city = weather_cities.id)
                                     WHERE weather.id = ?
                                    ''', (w_id,))
        result = self.connector.cursor.fetchonemap()
        self.connector.cursor.close()
        return result

    def create(self, city_id, forecast_date, avg_temp, avg_pressure, avg_rainfall):
        try:
            self.connector.cursor.execute('''INSERT INTO WEATHER (id_city, forecast_date, avg_temp, avg_pressure, avg_rainfall) VALUES (?,?,?,?,?)''', (city_id, forecast_date, avg_temp, avg_pressure, avg_rainfall))
            self.connector.dataset.commit()
            return True
        except fdb.Error as e:
            self.connector.dataset.rollback()
            return f"{e}"

    def update(self, city_id, forecast_date, avg_temp, avg_pressure, avg_rainfall, id):
        try:
            self.connector.cursor.execute('''
                                             UPDATE WEATHER SET id_city=?, forecast_date=?, avg_temp=?, avg_pressure=?, avg_rainfall=?
                                             WHERE ID = ?
                                             ''', (city_id, forecast_date, avg_temp, avg_pressure, avg_rainfall, id))
            self.connector.dataset.commit()
            return True
        except fdb.Error as e:
            print(e)
            self.connector.dataset.rollback()

    def delete(self, id):
        try:
        # Спасибо, Дмитрий Сергеевич
            print(id)
            self.connector.cursor.execute('''DELETE FROM weather WHERE ID=?''', (id, ))
            self.connector.dataset.commit()
            return True
        except fdb.Error as e:
            print(e)
            self.connector.dataset.rollback()

class WeatherCity(BaseDBView):
    def get_all(self):
        self.connector.cursor.execute('''
                                        SELECT id, name_city
                                    from weather_cities
                                     ''')
        result = self.connector.cursor.fetchallmap()
        self.connector.cursor.close()
        return result