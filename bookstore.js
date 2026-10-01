// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
// paste your drop and insertMany commands here
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
// paste your drop and insertMany commands here
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
// paste your find commands here
db.authors.find()
db.books.find()

// Step 6: insert two new books
// paste your insert commands here
db.books.insertMany([ 
    { title: "book 5", published_year: 1999, author_ids: ["author_001"] }, 
    { title: "book 6", published_year: 1999, author_ids: ["author_004"] } 
])

// Step 7: add missing authors
// paste your insert commands here
db.authors.insertOne({ 
    _id: "author_004", 
    name: "Author Four", 
    nationality: "Korean", 
    bio: { short: "this is a short", 
        long: "this is a long"} 
    })

// Step 8: filter books by a list of authors
// paste your find command here
db.books.find({ 
    author_ids: { 
        $in: ["author_004", "author_001"] 
    } 
})