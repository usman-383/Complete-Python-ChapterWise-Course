
#Match case

def http_status(ststus):
    match http_status:
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "Internl server error"
        case _:
            return "Unknown status"
        
print(http_status(5007))