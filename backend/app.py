from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "recipesdb")
DB_USER = os.environ.get("DB_USER", "appuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "apppassword")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


@app.route("/recipes", methods=["GET"])
def get_recipes():
    conn = get_connection()
    cur = conn.cursor()

    # return full recipe data
    cur.execute("SELECT id, name, ingredients, instructions FROM recipes;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    recipes = [
        {
            "id": r[0],
            "name": r[1],
            "ingredients": r[2],
            "instructions": r[3],
        }
        for r in rows
    ]
    return jsonify(recipes)


@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT name, ingredients, instructions FROM recipes WHERE id = %s;",
        (recipe_id,),
    )
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return jsonify({"error": "Recipe not found"}), 404

    recipe = {
        "name": row[0],
        "ingredients": row[1],
        "instructions": row[2],
    }
    return jsonify(recipe)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})
