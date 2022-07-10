from app.api import *
router, repository = init_controller('product')


@router.get("/", response_model=List[ProductResponse])
def get_all(database: Session = Depends(get_db)):
    return repository.get_all(database=database)


@router.get("/{id}", response_model=ProductResponse)
def get_by_id(id: int, database: Session = Depends(get_db)):
    return repository.get_by_id(database=database, id=id)


@router.post("/", response_model=ProductResponse)
def add(product: ProductRequest, database: Session = Depends(get_db)):
    return repository.add(database=database, product=product)


@router.put("/{id}", response_model=ProductResponse)
def update(product: ProductRequest, id: int, database: Session = Depends(get_db)):
    return repository.update(database=database, payload=product, id=id)


@router.delete("/{id}")
def delete(id: int, database: Session = Depends(get_db)):
    return repository.delete(database=database, id=id)
