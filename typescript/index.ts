let nombre = 'cesar'; 
let apellido: string = 'cordero'; 
let edad: number = 24; 
let casado: boolean = false;
let fechaNacimiento: Date = new Date();
let extra: any = 'cualquier cosa';
let sinDefinir: undefined = undefined;
let nulo: null = null;


let numeros: number[] = [1,2,3,4,5];

let persona: {nombre: string, apellido: string, edad: number} = {
    nombre: 'cesar',
    apellido: 'cordero',
    edad: 24
}

function sumar(a: number, b: number): number {
    return a + b;
}

console.log(sumar(1,2));

class Persona{
    nombre: string;
    apellido: string;
    edad: number;
    constructor(nombre: string, apellido: string, edad: number){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }
}

interface IPersona{ 
    nombre: string;
    apellido: string;
    edad?: number;
}

let persona2: IPersona = {
    nombre: 'cesar',
    apellido: 'cordero',
    edad: 24
}

let persona3: IPersona = {
    nombre: 'Ana',
    apellido: 'cordero'
}

