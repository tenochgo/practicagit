from flask import Flask, jsonify

app = Flask(__name__)

cat_facts = [
    "Cats have five toes on their front paws, but only four toes on their back paws.",
    "A group of cats is called a clowder.",
    "Cats can rotate their ears 180 degrees.",
    "The world's largest cat measured 48.5 inches long.",
    "Cats sleep for 70% of their lives."
]

@app.route('/cat-facts', methods=['GET'])
def get_cat_facts():
    return jsonify(cat_facts)

if __name__ == '__main__':
    app.run(debug=True)