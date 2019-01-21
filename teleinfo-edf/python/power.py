
import sqlite3
import datetime

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class TeleinfoEdf(ABC.abc)

    def __init__(self):
        pass

    def getPower (self, int: numberOfDays):
        """
        //
        //  recupere les donnees de puissance des $nb_days derniers jours et les met en forme pour les affichers sur le graphique
        //
        
        global $sqlite;
        $months    = array('01' => 'janv', '02' => 'fev', '03' => 'mars', '04' => 'avril', '05' => 'mai', '06' => 'juin', '07' => 'juil', '08' => 'aout', '09' => 'sept', '10' => 'oct', '11' => 'nov', '12' => 'dec');
        $now  = time();
        """
        db = sqlite3.connect("teleinfo-edf.sqlite")
        delta = datetime.timedelta(days=(-1*numberOfDays))
        dt = datetime.datetime(delta.year,delta.month,delta.day).timestamp()
        nw = datetime.datetime.now().timestamp()
        d = datetime.timedelta(days=(1*7)).total_seconds()
        min = nw-d

        db.row_factory = dict_factory
        cursor = db.cursor()
        db.execute("SELECT * FROM puissance WHERE timestamp > "+str(int(min))+" and timestamp < "+str(int(nw))+" ORDER BY timestamp ASC;")
        results = cursor.fetchall()
        print results
        db.close()
 
        """
        $past = strtotime("-$nb_days day", $now);

        $db = new SQLite3($sqlite);
        $results = $db->query("SELECT * FROM puissance WHERE timestamp > $past ORDER BY timestamp ASC;");

        $sums = array();
        $days = array();
        $datas = array();

        while($row = $results->fetchArray(SQLITE3_ASSOC)){
        $year   = date("Y", $row['timestamp']);
        $month  = date("n", $row['timestamp']-1);
        $day    = date("j", $row['timestamp']);
        $hour   = date("G", $row['timestamp']);
        $minute = date("i", $row['timestamp']);
        $second = date("s", $row['timestamp']);
        $datas[] = "[{v:new Date($year, $month, $day, $hour, $minute, $second), f:'".date("j", $row['timestamp'])." ".$months[date("m", $row['timestamp'])]." ".date("H\hi", $row['timestamp'])."'}, {v:".$row['va'].", f:'".$row['va']." V.A'}, {v:".$row['watt'].", f:'".$row['watt']." kW'}]";

        }

        return implode(', ', $datas);
        }
        """
        
        def getConso (self, int: numberOfDays) {
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
