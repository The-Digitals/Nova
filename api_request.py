import cohere

co = cohere.Client('usz2oJbxvPMthPDMUJT5bGW8UG4zFpBnmy8KEFf7')

text = "Θέλω να μου φτίαξεις μια περίληψη 100 λέξεων του κειμένου: "

context = """Η Παγκόσμια Ημέρα Βιβλίου έρχεται (23/4) και τα Novacinema στο πλαίσιο των μεγάλων αφιερωμάτων που προσφέρουν στους συνδρομητές τους, παρουσιάζουν το «Book Club», προκειμένου οι σινεφίλ να απολαύσουν σπουδαίες κινηματογραφικές μεταφορές διάσημων βιβλίων!Από τη Δευτέρα 22 έως την Κυριακή 28 Απριλίου, συντονιστείτε κάθε βράδυ στις 22:00 και απολαύστε δύο ταινίες back to back: «The Reader», «Fear and Loathing in Las Vegas», «Pride and Prejudice», «Call Me By Your Name», «The Danish Girl», «Το Ακρωτήρι του Φόβου», «She Said», «The Subtle Art of not Giving a F*ck», «Atonement», «Love Again», «Lyle, Lyle, Crocodile», «Where the Crawdads Sing», «A Man Called Otto», «Bridget Jones’s Diary».

Οι σινεφίλ ετοιμάζονται να «ταξιδέψουν» στις οθόνες τους με το αφιέρωμα στην Παγκόσμια Ημέρα του Βιβλίου, που περιλαμβάνει:

Δευτέρα 22 Απριλίου
1-The-Reader
2-Fear-and-Loathing-in-Las-Vegas
22:00 Τη ρομαντική δραματική ταινία «Σφραγισμένα Χείλη (The Reader 2008, διάρκειας 119’)» με τους Kate Winslet, Ralph Fiennes, Bruno Ganz, Jeanette Hain σε σκηνοθεσία του Stephen Daldry. Στη μεταπολεμική Γερμανία, ένας άντρας ανακαλύπτει ότι η γυναίκα με την οποία είχε σχέση πριν χρόνια είναι κατηγορούμενη σε δίκη για εγκλήματα πολέμου. Η ταινία απέσπασε Οσκαρ και Χρυσή Σφαίρα και βασίζεται στο ομώνυμο βιβλίο του Bernhard Schlink.

00:10 Την κωμική περιπέτεια «Φόβος και Παράνοια στο Λας Βέγκας (Fear and Loathing in Las Vegas, 1998, διάρκειας 114’)» με τους Johnny Depp, Benicio Del Toro, Tobey Maguire σε σκηνοθεσία του Terry Gilliam, βασισμένη στο ομώνυμο βιβλίο του Hunter S. Thompson. Το 'αμερικανικό όνειρο' δεν είναι πάντα εφικτός στόχος. Δύο άντρες προσπαθούν με όλη τους την ψυχή να το κάνουν πραγματικότητα, και ξεκινούν ένα παράξενο ταξίδι που αγγίζει τα όρια της παράνοιας.
Τρίτη 23 Απριλίου
3-Pride-And-Prejudice
4-Call-me-by-your-name
22:00 Τη ρομαντική ταινία «Περηφάνια και Προκατάληψη (Pride and Prejudice, 2005, διάρκειας 105’)» με τους Keira Knightley, Matthew Macfadyen, Rosamund Pike, Donald Sutherland, σε σκηνοθεσία του Joe Wright. Στη βικτοριανή Αγγλία, ένας ανομολόγητος έρωτας γεννιέται ανάμεσα σε μια ταπεινής καταγωγής κοπέλα κι έναν αλαζονικό ευγενή, σε μία ταινία που προτάθηκε για 4 Όσκαρ, και βασίζεται στο διάσημο ομώνυμο βιβλί
"""
message = text + context

response = co.chat(
	message = message, 
	model = "command", 
	temperature = 0.1
)

answer = response.text
print(answer)

