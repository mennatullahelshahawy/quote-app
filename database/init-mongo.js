db = db.getSiblingDB('quotes-app');
db.quotes.insertMany([
{
    quote:"The only way to do great work is to love what you do.",
    author:"Steve Jobs",
    color:"#2C3E50"
},
{
    quote:"In the middle of every difficulty lies opportunity.",
    author:"Albert Einstein",
    color:"#16A085"
},
{
    quote: "Code is like humor. When you have to explain it, it’s bad.",
    author: "Cory House",
    color: "#8E44AD"
  },
  {
    quote: "Simplicity is prerequisite for reliability.",
    author: "Edsger W. Dijkstra",
    color: "#2980B9"
  },
  {
    quote: "Make it work, make it right, make it fast.",
    author: "Kent Beck",
    color: "#D35400"
  }
]
);
