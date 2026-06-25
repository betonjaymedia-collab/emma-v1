import pool from "./client";

export const insertComponent = async (component: any) => {
  const query = `
    INSERT INTO components (
      id, name, status, definition, relies_on, impacts, updated_at
    )
    VALUES ($1, $2, $3, $4, $5, $6, $7)
  `;

  const values = [
    component.id,
    component.name,
    component.status,
    component.definition,
    component.dependencies.relies_on,
    component.dependencies.impacts,
    component.updatedAt,
  ];

  await pool.query(query, values);
};
``