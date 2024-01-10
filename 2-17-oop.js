class Wall {
  constructor(material, height) {
    this.material = material;
    this.height = height;
  }
 
  toString() {
    return `Material is ${this.material}, height = ${this.height} ft.`;
  }
}
 
class Furniture {
  constructor(name, cost) {
    this.name = name;
    this.cost = cost;
  }
 
  toString() {
    return `name = ${this.name}, cost = ${this.cost}$`;
  }
}
 
class Apartment {
  constructor(street, apartmentNo, material, height, furniture) {
    this.street = street;
    this.apartmentNo = apartmentNo;
    this.walls = new Wall(material, height);
    this.furniture = furniture;
  }
 
  toString() {
    return `The address is '${this.street} St' ${
      this.apartmentNo
    }, walls ${this.walls.toString()}, furniture=[\n${this.furniture.join(
      "\n"
    )}]`;
  }
 
  getTotalFurnitureCost() {
    return this.furniture.reduce((cost, element) => cost + element.cost, 0);
  }
}
 
const furniture = [
  new Furniture("bed", 150),
  new Furniture("cupboard", 250),
  new Furniture("table", 35),
  new Furniture("armchair", 80),
];
 
const flat = new Apartment("Bronco", 3050, "brick", 23, furniture);
 
console.log("Information about the apartment: " + flat.toString());
console.log(`Total furniture cost is ${flat.getTotalFurnitureCost()}`);