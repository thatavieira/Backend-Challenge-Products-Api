from src.controllers import *
router, repository = init_controller('category')


@router.get("/", response_model=List[CategoryResponse])
def get_all(database: Session = Depends(get_db)):
    return repository.get_all(database=database)


@router.get("/{id}", response_model=CategoryResponse)
def get_by_id(id: int, database: Session = Depends(get_db)):
    return repository.get_by_id(database=database, id=id)


@router.post("/", response_model=CategoryResponse)
def add(name: str, database: Session = Depends(get_db)):
    return repository.add(database=database, name=name)


@router.put("/{id}", response_model=CategoryResponse)
def update(category: CategoryRequest, id=id, database: Session = Depends(get_db)):
    return repository.update(database=database, category=category, id=id)


@router.delete("/{id}", response_model=CategoryResponse)
def delete(id: int, database: Session = Depends(get_db)):
    return repository.delete(database=database, id=id)