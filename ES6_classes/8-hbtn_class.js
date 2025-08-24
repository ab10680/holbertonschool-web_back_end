export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // size
  valueOf() {
    return this._size;
  }

  // location
  toString() {
    return this._location;
  }
}
