import random
subject=[
    "CarryMinati",
    "Elvish Yadav",
    "Ashish Chanchlani",
    "Bhuvan Bam",
    "Technical Guruji",
    "Triggered Insaan",
    "Dhruv Rathee",
    "Prajakta Koli",
    "Mumbiker Nikhil",
    "Amit Bhadana",
    "Round2hell",
    "Harsh Beniwal",
    "Sourav Joshi",
    "Gaurav Taneja",
    "Nischay Malhan"
]

action=[
    "Got kicked by a donkey",
    "Got chased by a goat",
    "Slipped on a banana peel",
    "Got scared of a rubber snake",
    "Ran away from a tiny puppy",
    "Got hit by a flying pillow",
    "Tripped while trying to act cool",
    "Fell off a chair dramatically",
    "Got splashed with a bucket of water",
    "Got chased by a swarm of bees",
    "Got stuck inside a cardboard box",
    "Got attacked by a pillow during pillow fight",
    "Got scared by their own shadow",
    "Fell into mud while showing attitude",
    "Got locked outside the house"
]

places_with_at = [
    "at Jaipur",
    "at Varanasi",
    "at Delhi",
    "at Mumbai",
    "at Bengaluru",
    "at Hyderabad",
    "at Kolkata",
    "at Chennai",
    "at Lucknow",
    "at Agra",
    "at Udaipur",
    "at Amritsar",
    "at Goa",
    "at Shimla",
    "at Manali"
]



while(True):
    a=random.choice(subject)
    b=random.choice(action)
    c=random.choice(places_with_at)
    
    comb=a+" "+b+" "+c
    print("Breaking News:- "+comb)
    print(" ")
    st=input(" can i give u some more news:- YES OR NO in capital letter")
    
    if(st=="NO"):
        break
    
print("Goodbye")
    
