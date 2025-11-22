CREATE TABLE IF NOT EXISTS recipes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);

INSERT INTO recipes (name, ingredients, instructions) VALUES
(
    'Pancakes',
    'Flour, Milk, Eggs, Sugar, Butter',
    '1. Mix ingredients\n2. Heat pan\n3. Pour batter\n4. Flip and serve'
),
(
    'Spaghetti Alfredo',
    'Spaghetti, Butter, Cream, Garlic, Parmesan',
    '1. Boil pasta\n2. Prepare sauce\n3. Mix together\n4. Serve hot'
),
(
    'Salad Bowl',
    'Lettuce, Tomato, Cucumber, Olive oil, Lemon juice',
    '1. Chop veggies\n2. Mix in bowl\n3. Add dressing\n4. Enjoy'
);
