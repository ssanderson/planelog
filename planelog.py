import csv
from pprint import pprint as pp

def interpreter(filename="planelog.csv"):

    reader = csv.DictReader(open(filename))
    fields = reader.fieldnames
    entries = list(reader)

    preamble(fields, entries)
    while(True):
        query = build_query(raw_input("Enter a Query: "))
        process_query(query, entries)

def preamble(fields, entries):
    
    print('')
    print("Welcome to the Aircraft Flight Log of Alan H. Strawer")
    print("You may search the log by the following fields:")
    print('')
    
    for key in fields:
        # Searching by comments would be a pain in the ass as written.
        if key == 'Comments':
            continue
        print("'%s'" % key)
    
    print('')

    print("For example, to see all flights that occurred on December 19th, 1990:")
    print('')
    print("Enter a Query: Date=12/19/90")
    matches = get_matches(entries, Date="12/19/90")
    print('')
    for match in matches:
        pp(match)
        print('')
        
def build_query(s):
    if s == 'quit':
        return s
    
    query = {}
    kv_list = s.split(',')
    for kv in kv_list:
        try:
            k, v = tuple(kv.split('='))
        except:
            print "Error trying to process the following query: <%s>" % kv
            return None
        query[k] = v
    
    return query

def process_query(query, entries):
    if query == 'quit':
        exit(0)
    if query == None:
        return
    assert isinstance(query, dict)

    matches = get_matches(entries, **query)
    print('')
    print('Matches:')
    for match in matches:
        print('')
        pp(match)
    print('')

def get_matches(entries, **kwargs):
    
    def matches():
        for entry in entries:
            for key, value in kwargs.iteritems():
                if entry.get(key) != value:
                    break
                yield entry
    return matches()
    
if __name__ == "__main__":
    interpreter()
    
    
    
