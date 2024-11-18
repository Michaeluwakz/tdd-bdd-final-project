# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product

class ProductFactory(factory.Factory):
    """Creates fake products for testing."""

    class Meta:
        model = Product

    name = FuzzyChoice(
        choices=[
            "Hat", "Pants", "Shirt", "Apple", "Banana",
            "Pots", "Towels", "Ford", "Chevy", "Hammer", "Wrench"
        ]
    )
    description = factory.Faker("text")
    price = FuzzyDecimal(0.5, 2000.0, precision=2)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=["UNKNOWN", "CLOTHS", "FOOD", "HOUSEWARES", "AUTOMOTIVE", "TOOLS"]
    )