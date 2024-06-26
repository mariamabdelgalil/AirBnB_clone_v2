#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents an Amenity in a MySQL database.

    Attributes:
        __tablename__: Table name for amenities in MySQL.
        name: The name of the amenity.
        place_amenities: Relationship with Place.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary="place_amenity", viewonly=False
    )
