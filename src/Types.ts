export interface Event {
  label: string;
}

export interface Item {
  name: string;
  imageFilename: string;
}

export interface Option {
  text: string;
  target: number;
  paragraph: number;
  requiredEvents?: Array<number>;
  excludingEvents?: Array<number>;
  requiredItems?: Array<number>;
  excludingItems?: Array<number>;
}

export interface Chapter {
  title: string;
  text: string;
  isEnding?: boolean;
  addsItems?: Array<number>;
  removesItems?: Array<number>;
  addsEvents?: Array<number>;
}
