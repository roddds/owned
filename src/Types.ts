export interface Event {
  name: string;
}

export interface Item {
  name: string;
  path: string;
}

export interface Option {
  text: string;
  target: number;
  requiredEvents?: number[];
  excludingEvents?: number[];
  requiredItems?: number[];
  excludingItems?: number[];
}

export interface Chapter {
  title: string;
  text: string;
  isEnding?: boolean;
  addsItems?: number[];
  removesItems?: number[];
  addsEvents?: number[];
  options: number[];
}

export interface Events {
  [key: string]: Event;
}

export interface Items {
  [key: string]: Item;
}

export interface Options {
  [key: string]: Option;
}

export interface Chapters {
  [key: string]: Chapter;
}

export interface BookData {
  event: Events;
  item: Items;
  option: Options;
  chapter: Chapters;
}
