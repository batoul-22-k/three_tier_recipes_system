apiVersion: v1
kind: Service
metadata:
  name: recipes-db
spec:
  selector:
    app: recipes-db
  ports:
    - port: 5432
      targetPort: 5432
