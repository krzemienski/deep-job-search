// Learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom'

// Mock sessionStorage
const mockStorage = {}
global.sessionStorage = {
  getItem: (key) => mockStorage[key],
  setItem: (key, value) => { mockStorage[key] = value },
  clear: () => { mockStorage = {} }
}
