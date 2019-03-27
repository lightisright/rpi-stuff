
import sqlite3
import datetime

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        if col[0] == 'timestamp':
            d['date'] = datetime.datetime.fromtimestamp(row[idx]).isoformat()
        else:
            d[col[0]] = row[idx]
    return d

def power_factory(cursor, row):
    # x1000 for HighCharts rendering
    return [row[0]*1000,row[4]]



class TeleinfoEdf():

    def __init__(self):
        pass

    def debug(self,msg: str):
        print(msg)

    def getPower(self, numberOfDays:int, start:datetime = datetime.datetime.now()):
        return self._getData(numberOfDays, power_factory, start)

    def _getData (self, numberOfDays:int, dict_factory, start:datetime = datetime.datetime.now()):
        
        db = sqlite3.connect("teleinfo-edf.sqlite")

        d2=start
        t2=d2.timestamp()

        delta = datetime.timedelta(days=(-1*numberOfDays)).total_seconds()
        t1=t2+delta
        d1=datetime.datetime.fromtimestamp(t1)
        
        self.debug(f"d1: {d1.isoformat()} - d2: {d2.isoformat()}")
        self.debug(f"t1: {t1} - t2: {t2}")

        req = f"SELECT * FROM puissance WHERE timestamp > {str(int(t1))} and timestamp < {str(int(t2))} ORDER BY timestamp ASC;"
        
        cursor = db.cursor()
        cursor.row_factory = dict_factory
        cursor.execute(req)
        
        result = cursor.fetchall()
        self.debug(result)
        db.close()
        return(result)
        
    def getConso (self, numberOfDays:int):
        return False
        """

         //
        //  recupere les donnees de consommation des $nb_days derniers jours et les met en forme pour les affichers sur le graphique
        //
        function getDatasConso ($nb_days) {
            global $sqlite;
            $months    = array('01' => 'janv', '02' => 'fev', '03' => 'mars', '04' => 'avril', '05' => 'mai', '06' => 'juin', '07' => 'juil', '08' => 'aout', '09' => 'sept', '10' => 'oct', '11' => 'nov', '12' => 'dec');
            $now  = time();
            $past = strtotime("-$nb_days day", $now);

            $db = new SQLite3($sqlite);
            $results = $db->query("SELECT * FROM conso WHERE timestamp > $past ORDER BY timestamp ASC;");

            $datas = array();

            while($row = $results->fetchArray(SQLITE3_ASSOC)){
            $day    = date("j", $row['timestamp'])." ".$months[date("m", $row['timestamp'])];
            $datas[] = "['".$day."', {v:".$row['daily_hp'].", f:'".$row['daily_hp']." kWh'}, {v:".$row['daily_hc'].", f:'".$row['daily_hc']." kWh'}]";
            }

            return implode(', ', $datas);
        }

        """
