from fastapi import HTTPException, status


def entity_not_found_ex(entity_id: int, entity_name: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity_name} #{entity_id} not found!",
    )


def table_reserved_ex(entity_id: int, entity_name: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=(f"The requested time slot for {entity_name} #{entity_id} is "
                f"already booked. Please choose a different date or time."),
    )
