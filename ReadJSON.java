import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.URL;
import java.net.URLConnection;
import java.io.FileWriter;

/*
	Reads a file from the url containing all cards and all their 
	attributes in a JSON format. Then writes all contents to a local
	file called cards_JSON.txt
	credit: https://github.com/Solumin/YGO-FM-FusionCalc
*/

public class ReadJSON{

    public static void main(String[] args) throws IOException {

        // Make a URL to the web page
        URL url = new URL("https://raw.githubusercontent.com/Solumin/YGO-FM-FusionCalc/master/data/Cards.json");

        // Get the input stream through URL Connection
        URLConnection con = url.openConnection();
        InputStream is = con.getInputStream();
		
        BufferedReader br = new BufferedReader(new InputStreamReader(is));

        String line = null;
		
		try {
			FileWriter myWriter = new FileWriter("cards_JSON.txt");
			int i = 0;
			while ((line = br.readLine()) != null) {
				/*if (line.equals("  {")) {
					i++;
					line = i + ": [";
				}
				else if (line.equals("  },")) {
					line = "   ],";
				}*/
				myWriter.write(line + "\n");
			}
			
			myWriter.close();
			System.out.println("Successfully wrote to the file.");
		} 
		catch (IOException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}

    }
}