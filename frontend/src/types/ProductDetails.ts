import { Product } from "./Product"

export interface ProductDetails {
  id: number,  
  model: {
    id: number,
    name: string,
    maxLength: number,
    category:	number
    fabric: string,
    description: string,
    date_added: string,
    slug: string,
  }
  color: string,
  size: ProductSize,
  fabric: string,
  stock: number,
  price: string,
  stripe_product_id: string,
  date_added: string,
  images: string[],
  sizes_available: string[],
  colors_available: string[],
  slug:	string,
  wishlist: boolean,   
}

export interface ProductSize {
  id: number,
  tag: string,
  value: string,
  length: number,
  width: number,
}

export interface ItemDetails {
  id: number,
  model: Product,
  color: string,
  size: ProductSize,
  slug:	string,
  stock: number,
  price: string,
  stripe_product_id: string,
  date_added: string,
  images: string[],
  sizes_available: string[],
  colors_available: string[],
  wishlist: boolean,
}