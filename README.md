***
Телеграмм бот предлагает пользователю найти подходящие его запросу 
отели с помощью API запросов на платформу Hotels.com.
***
Пользователь с помощью команд бота может выполнить следующие действия:
* Сначала вывести дешевые отели в городе (**/lowprice**)
* Сначала вывести дорогие отели в городе (**/highprice**)
* Поиск отелей по цене и расположению от центра (**/bestdeal**)
* Узнать историю поиска (последние 10 результатов) (**/history**)
***
### Команды бота:

1. **/start**
    * Запускает бота с приветственным сообщением
2. **/help**
    * Выводит все команды бота
3. **/lowprice**
    * Запрашивает город, дату заезда/выезда и находит отели в городе от 
     самых дешёвых к более дорогим
4. **/highprice**  
    * Запрашивает город, дату заезда/выезда и находит отели в городе от 
     самых дорогих в более дешёвым
5. **/bestdeal**
    * Запрашивает город, дату заезда/выезда, минимальное и максимальное 
    расстояние от центра, максимальную и минимальную цены и находит 
    отели в городе


###Запрос города
```
import requests

url = "https://hotels4.p.rapidapi.com/locations/v3/search"

querystring = {"q":"Чикаго","locale":"ru_RU"}

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

```
### Ответ
```
{
  "q": "Чикаго",
  "rid": "cf7358d235c04e5db9dc651a2ae89a69",
  "rc": "OK",
  "sr": [
    {
      "@type": "gaiaRegionResult",
      "index": "0",
      "gaiaId": "829",
      "type": "CITY",
      "regionNames": {
        "fullName": "Чикаго, Илинойс, США",
        "shortName": "Чикаго",
        "displayName": "Чикаго, Илинойс, США",
        "primaryDisplayName": "Чикаго",
        "secondaryDisplayName": "Илинойс, США",
        "lastSearchName": "Чикаго"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "829"
      },
      "coordinates": {
        "lat": "41.878113",
        "long": "-87.629799"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "CHI",
          "airportId": "6139044",
          "metrocode": "CHI",
          "multicity": "829"
        }
      }
    },
    {
      "@type": "gaiaRegionResult",
      "index": "1",
      "gaiaId": "800024",
      "type": "NEIGHBORHOOD",
      "regionNames": {
        "fullName": "Чикаго-Луп, Чикаго, Илинойс, США",
        "shortName": "Чикаго-Луп",
        "displayName": "Чикаго-Луп, Чикаго, Илинойс, США",
        "primaryDisplayName": "Чикаго-Луп",
        "secondaryDisplayName": "Чикаго, Илинойс, США",
        "lastSearchName": "Чикаго-Луп"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "800024"
      },
      "coordinates": {
        "lat": "41.883736",
        "long": "-87.62886"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "CHI",
          "airportId": "6139044",
          "metrocode": "CHI",
          "multicity": "829"
        }
      }
    },
    {
      "@type": "gaiaRegionResult",
      "index": "2",
      "gaiaId": "4477519",
      "type": "AIRPORT",
      "regionNames": {
        "fullName": "Чикаго, Иллинойс, США (ORD-O'Хара, международный)",
        "shortName": "Чикаго, Иллинойс (ORD-O'Хара, международный)",
        "displayName": "Чикаго (ORD - O'Хара, международный), Иллинойс, США",
        "primaryDisplayName": "Чикаго (ORD - O'Хара, международный)",
        "secondaryDisplayName": "Иллинойс, США",
        "lastSearchName": "Чикаго (ORD - O'Хара, международный)"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "4477519"
      },
      "coordinates": {
        "lat": "41.976977",
        "long": "-87.90481"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "ORD",
          "airportId": "4477519",
          "metrocode": "CHI",
          "multicity": "178248"
        }
      },
      "isMinorAirport": "false"
    },
    {
      "@type": "gaiaRegionResult",
      "index": "3",
      "gaiaId": "6027439",
      "type": "AIRPORT",
      "regionNames": {
        "fullName": "Чикаго, Иллинойс, США (DPA-Дупейдж)",
        "shortName": "Чикаго, Иллинойс (DPA-Дупейдж)",
        "displayName": "Чикаго (DPA - Дупейдж), Иллинойс, США",
        "primaryDisplayName": "Чикаго (DPA - Дупейдж)",
        "secondaryDisplayName": "Иллинойс, США",
        "lastSearchName": "Чикаго (DPA - Дупейдж)"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "6027439"
      },
      "coordinates": {
        "lat": "41.906721",
        "long": "-88.255336"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "DPA",
          "airportId": "6027439",
          "metrocode": "CHI",
          "multicity": "178248"
        }
      },
      "isMinorAirport": "false"
    },
    {
      "@type": "gaiaRegionResult",
      "index": "4",
      "gaiaId": "6350699",
      "type": "NEIGHBORHOOD",
      "regionNames": {
        "fullName": "Центр Чикаго, Чикаго, Илинойс, США",
        "shortName": "Центр Чикаго",
        "displayName": "Центр Чикаго, Чикаго, Илинойс, США",
        "primaryDisplayName": "Центр Чикаго",
        "secondaryDisplayName": "Чикаго, Илинойс, США",
        "lastSearchName": "Центр Чикаго"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "6350699"
      },
      "coordinates": {
        "lat": "41.885969845574834",
        "long": "-87.62933540465228"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "CHI",
          "airportId": "6139044",
          "metrocode": "CHI",
          "multicity": "829"
        }
      }
    },
    {
      "@type": "gaiaRegionResult",
      "index": "5",
      "gaiaId": "6132188",
      "type": "NEIGHBORHOOD",
      "regionNames": {
        "fullName": "Чикаго-Лон, Чикаго, Илинойс, США",
        "shortName": "Чикаго-Лон",
        "displayName": "Чикаго-Лон, Чикаго, Илинойс, США",
        "primaryDisplayName": "Чикаго-Лон",
        "secondaryDisplayName": "Чикаго, Илинойс, США",
        "lastSearchName": "Чикаго-Лон"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "6132188"
      },
      "coordinates": {
        "lat": "41.77173540220963",
        "long": "-87.69581950287477"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "CHI",
          "airportId": "6139044",
          "metrocode": "CHI",
          "multicity": "829"
        }
      }
    },
    {
      "@type": "gaiaRegionResult",
      "index": "6",
      "gaiaId": "89157",
      "type": "CITY",
      "regionNames": {
        "fullName": "Чикаго-Хейтс, Илинойс, США",
        "shortName": "Чикаго-Хейтс",
        "displayName": "Чикаго-Хейтс, Илинойс, США",
        "primaryDisplayName": "Чикаго-Хейтс",
        "secondaryDisplayName": "Илинойс, США",
        "lastSearchName": "Чикаго-Хейтс"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "89157"
      },
      "coordinates": {
        "lat": "41.506146",
        "long": "-87.635597"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "CHI",
          "airportId": "6139044",
          "metrocode": "CHI",
          "multicity": "829"
        }
      }
    },
    {
      "@type": "gaiaRegionResult",
      "index": "7",
      "gaiaId": "6031352",
      "type": "AIRPORT",
      "regionNames": {
        "fullName": "Чикаго, Иллинойс, США (PWK-Чикаго, административный)",
        "shortName": "Чикаго, Иллинойс (PWK-Чикаго, административный)",
        "displayName": "Чикаго (PWK - Чикаго, административный), Иллинойс, США",
        "primaryDisplayName": "Чикаго (PWK - Чикаго, административный)",
        "secondaryDisplayName": "Иллинойс, США",
        "lastSearchName": "Чикаго (PWK - Чикаго, административный)"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "6031352"
      },
      "coordinates": {
        "lat": "42.11674",
        "long": "-87.89938"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "PWK",
          "airportId": "6031352",
          "metrocode": "CHI",
          "multicity": "178248"
        }
      },
      "isMinorAirport": "false"
    },
    {
      "@type": "gaiaRegionResult",
      "index": "8",
      "gaiaId": "89160",
      "type": "CITY",
      "regionNames": {
        "fullName": "Чикаго-Ридж, Илинойс, США",
        "shortName": "Чикаго-Ридж",
        "displayName": "Чикаго-Ридж, Илинойс, США",
        "primaryDisplayName": "Чикаго-Ридж",
        "secondaryDisplayName": "Илинойс, США",
        "lastSearchName": "Чикаго-Ридж"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "89160"
      },
      "coordinates": {
        "lat": "41.701422",
        "long": "-87.77922"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "CHI",
          "airportId": "6139044",
          "metrocode": "CHI",
          "multicity": "829"
        }
      }
    },
    {
      "@type": "gaiaRegionResult",
      "index": "9",
      "gaiaId": "5719117",
      "type": "AIRPORT",
      "regionNames": {
        "fullName": "Чикаго, Иллинойс, США (MDW-Мидвей, международный)",
        "shortName": "Чикаго, Иллинойс (MDW-Мидвей, международный)",
        "displayName": "Чикаго (MDW - Мидвей, международный), Иллинойс, США",
        "primaryDisplayName": "Чикаго (MDW - Мидвей, международный)",
        "secondaryDisplayName": "Иллинойс, США",
        "lastSearchName": "Чикаго (MDW - Мидвей, международный)"
      },
      "essId": {
        "sourceName": "GAI",
        "sourceId": "5719117"
      },
      "coordinates": {
        "lat": "41.7884",
        "long": "-87.74101"
      },
      "hierarchyInfo": {
        "country": {
          "name": "Соединенные Штаты",
          "isoCode2": "US",
          "isoCode3": "USA"
        },
        "airport": {
          "airportCode": "MDW",
          "airportId": "5719117",
          "metrocode": "CHI",
          "multicity": "178248"
        }
      },
      "isMinorAirport": "false"
    }
  ]
}

```

### Запрос отелей в городе
```
import requests

url = "https://hotels4.p.rapidapi.com/properties/v2/list"

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"destination": { "regionId": "829" },
	"checkInDate": {
		"day": 10,
		"month": 5,
		"year": 2024
	},
	"checkOutDate": {
		"day": 15,
		"month": 5,
		"year": 2024
	},
	"rooms": [
		{
			"adults": 2,
			"children": [{ "age": 5 }, { "age": 7 }]
		}
	],
	"resultsStartingIndex": 0,
	"resultsSize": 3,
	"sort": "PRICE_LOW_TO_HIGH",
	"filters": { "price": {
			"max": 150,
			"min": 100
		} }
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

```

### Ответ
```
{
  "data": {
    "propertySearch": {
      "__typename": "PropertySearchResults",
      "filterMetadata": {
        "__typename": "PropertyFilterMetadata",
        "amenities": [
          {
            "__typename": "PropertyAmenityValue",
            "id": 7
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 14
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 82
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 16
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 19
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 27
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 66
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 80
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 81
          },
          {
            "__typename": "PropertyAmenityValue",
            "id": 84
          }
        ],
        "neighborhoods": [
          {
            "__typename": "Neighborhood",
            "name": "Chicago (and vicinity)",
            "regionId": "178248"
          },
          {
            "__typename": "Neighborhood",
            "name": "Downtown Chicago",
            "regionId": "6350699"
          },
          {
            "__typename": "Neighborhood",
            "name": "The Loop",
            "regionId": "800024"
          },
          {
            "__typename": "Neighborhood",
            "name": "Magnificent Mile",
            "regionId": "800025"
          },
          {
            "__typename": "Neighborhood",
            "name": "River North",
            "regionId": "6350695"
          },
          {
            "__typename": "Neighborhood",
            "name": "Gold Coast",
            "regionId": "6130105"
          },
          {
            "__typename": "Neighborhood",
            "name": "Lakeview",
            "regionId": "178166"
          },
          {
            "__typename": "Neighborhood",
            "name": "Hyde Park",
            "regionId": "117842"
          },
          {
            "__typename": "Neighborhood",
            "name": "Schaumburg",
            "regionId": "8107"
          },
          {
            "__typename": "Neighborhood",
            "name": "Gurnee",
            "regionId": "8240"
          },
          {
            "__typename": "Neighborhood",
            "name": "Naperville",
            "regionId": "9009"
          },
          {
            "__typename": "Neighborhood",
            "name": "South Loop",
            "regionId": "6130108"
          },
          {
            "__typename": "Neighborhood",
            "name": "Lincoln Park",
            "regionId": "6059328"
          },
          {
            "__typename": "Neighborhood",
            "name": "Wrigleyville",
            "regionId": "6338684"
          },
          {
            "__typename": "Neighborhood",
            "name": "Rosemont",
            "regionId": "7581"
          },
          {
            "__typename": "Neighborhood",
            "name": "West Loop",
            "regionId": "553248634029130868"
          },
          {
            "__typename": "Neighborhood",
            "name": "O'Hare",
            "regionId": "553248635074842747"
          },
          {
            "__typename": "Neighborhood",
            "name": "Aurora",
            "regionId": "6186"
          },
          {
            "__typename": "Neighborhood",
            "name": "Chicago, IL (ORD-O'Hare Intl.)",
            "regionId": "4477519"
          },
          {
            "__typename": "Neighborhood",
            "name": "Chicago Union Station",
            "regionId": "6129885"
          }
        ],
        "priceRange": {
          "__typename": "PriceRange",
          "max": 101.14,
          "min": 100.31
        }
      },
      "universalSortAndFilter": {
        "__typename": "ShoppingSortAndFilters",
        "toolbar": {
          "__typename": "UIToolbar",
          "primary": "Sort & Filter",
          "actions": {
            "__typename": "UIToolbarActions",
            "primary": {
              "__typename": "UITertiaryButton",
              "primary": null,
              "action": {
                "__typename": "ShoppingSortAndFilterAction",
                "actionType": "CLOSE_AND_DO_NOT_APPLY",
                "accessibility": null,
                "analytics": {
                  "__typename": "ClientSideAnalytics",
                  "linkName": "close search filters dialog",
                  "referrerId": "HOT.SR.CloseFilterDialog.Close"
                }
              }
            },
            "secondaries": [
              {
                "__typename": "UITertiaryButton",
                "primary": "Clear",
                "disabled": false,
                "action": {
                  "__typename": "ShoppingSortAndFilterAction",
                  "actionType": "CLEAR_DATA",
                  "accessibility": "All selections now cleared",
                  "analytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "clear all selections",
                    "referrerId": "HOT.SR.ClearFilters"
                  }
                }
              }
            ]
          }
        },
        "revealAction": {
          "__typename": "UISecondaryFloatingActionButton",
          "primary": "Sort & Filter",
          "action": {
            "__typename": "ShoppingSortAndFilterAction",
            "actionType": "OPEN_MODAL",
            "accessibility": null,
            "analytics": {
              "__typename": "ClientSideAnalytics",
              "linkName": "Launch filters takeover",
              "referrerId": "HOT.SR:FilterControl"
            }
          },
          "accessibility": "1 filter applied. Change sort or apply more filters.",
          "badge": 1,
          "disabled": false,
          "icon": {
            "__typename": "Icon",
            "id": "tune",
            "description": "reveals sort and filter window",
            "size": null,
            "token": "icon__tune",
            "theme": null
          }
        },
        "applyAction": {
          "__typename": "UIPrimaryFloatingActionButton",
          "primary": "Done",
          "action": {
            "__typename": "ShoppingSortAndFilterAction",
            "actionType": "CLOSE_AND_APPLY",
            "accessibility": null,
            "analytics": {
              "__typename": "ClientSideAnalytics",
              "linkName": "done search filters dialog",
              "referrerId": "HOT.SR.FilterControlDone"
            }
          },
          "accessibility": "Apply and close Sort and Filter",
          "badge": null,
          "disabled": false,
          "icon": null
        },
        "filterSections": [
          {
            "__typename": "ShoppingSortAndFilterSection",
            "title": "Search by property name",
            "fields": [
              {
                "__typename": "ShoppingTextInputField",
                "primary": null,
                "secondary": null,
                "action": {
                  "__typename": "ShoppingSortAndFilterAction",
                  "actionType": "OPEN_MODAL",
                  "accessibility": null,
                  "analytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "id": "hotelName",
                "label": null,
                "placeholder": "e.g. Marriott",
                "selected": null,
                "typeaheadInfo": {
                  "__typename": "TypeaheadInfo",
                  "client": "Hotels.Search",
                  "isDestination": true,
                  "lineOfBusiness": "hotels",
                  "maxNumberOfResults": 10,
                  "packageType": null,
                  "personalize": false,
                  "regionType": 128,
                  "typeaheadFeatures": "ta_hierarchy|postal_code|contextual_ta|consistent_display"
                },
                "icon": {
                  "__typename": "Icon",
                  "id": "search",
                  "description": "magnifying glass",
                  "size": null,
                  "token": "icon__search",
                  "theme": null
                },
                "analytics": {
                  "__typename": "ClientSideAnalytics",
                  "linkName": "hotelName.",
                  "referrerId": "HOT.SR.hotelName."
                }
              }
            ]
          },
          {
            "__typename": "ShoppingSortAndFilterSection",
            "title": "Filter by",
            "fields": [
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "Popular filters",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 10,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "mealPlan",
                    "primary": "Breakfast included",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "FREE_BREAKFAST",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.FREE_BREAKFAST",
                      "referrerId": "HOT.SR.popularFilter.mealPlan.FREE_BREAKFAST.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.FREE_BREAKFAST",
                      "referrerId": "HOT.SR.popularFilter.mealPlan.FREE_BREAKFAST.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Pool",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "pool",
                      "description": "",
                      "size": null,
                      "token": "icon__pool",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "POOL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.POOL",
                      "referrerId": "HOT.SR.popularFilter.amenities.POOL.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.POOL",
                      "referrerId": "HOT.SR.popularFilter.amenities.POOL.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Downtown Chicago",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "6350699",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6350699",
                      "referrerId": "HOT.SR.popularFilter.regionId.6350699.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6350699",
                      "referrerId": "HOT.SR.popularFilter.regionId.6350699.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Kitchen",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "kitchen",
                      "description": "",
                      "size": null,
                      "token": "icon__kitchen",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "KITCHEN_KITCHENETTE",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.KITCHEN_KITCHENETTE",
                      "referrerId": "HOT.SR.popularFilter.amenities.KITCHEN_KITCHENETTE.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.KITCHEN_KITCHENETTE",
                      "referrerId": "HOT.SR.popularFilter.amenities.KITCHEN_KITCHENETTE.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Hotel",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "HOTEL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.HOTEL",
                      "referrerId": "HOT.SR.popularFilter.lodging.HOTEL.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.HOTEL",
                      "referrerId": "HOT.SR.popularFilter.lodging.HOTEL.false:4"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingRangeField",
                "primary": "Price per night",
                "secondary": null,
                "range": {
                  "__typename": "ShoppingRangeFilterOption",
                  "id": "price",
                  "primary": "Less than $1,000",
                  "secondary": null,
                  "icon": null,
                  "analytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "price.",
                    "referrerId": "HOT.SR.price."
                  },
                  "selected": {
                    "__typename": "RangeValue",
                    "id": "price",
                    "min": 0,
                    "max": 1000
                  },
                  "characteristics": {
                    "__typename": "ShoppingRangeCharacteristics",
                    "min": 0,
                    "max": 1000,
                    "step": 100,
                    "labels": [
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$0",
                        "value": 0
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$100",
                        "value": 100
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$200",
                        "value": 200
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$300",
                        "value": 300
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$400",
                        "value": 400
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$500",
                        "value": 500
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$600",
                        "value": 600
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$700",
                        "value": 700
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$800",
                        "value": 800
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$900",
                        "value": 900
                      },
                      {
                        "__typename": "ShoppingRangeLabel",
                        "label": "$1,000+",
                        "value": 1000
                      }
                    ]
                  }
                }
              },
              {
                "__typename": "ShoppingSelectionField",
                "primary": "Guest rating",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 10,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "options": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "guestRating",
                    "primary": "Any",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "",
                    "description": null,
                    "selected": true,
                    "disabled": false,
                    "default": true,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.ANY",
                      "referrerId": "HOT.SR.guestRating.ANY.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.ANY",
                      "referrerId": "HOT.SR.guestRating.ANY.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "guestRating",
                    "primary": "Wonderful 9+",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "45",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.45",
                      "referrerId": "HOT.SR.guestRating.45.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.45",
                      "referrerId": "HOT.SR.guestRating.45.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "guestRating",
                    "primary": "Very good 8+",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "40",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.40",
                      "referrerId": "HOT.SR.guestRating.40.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.40",
                      "referrerId": "HOT.SR.guestRating.40.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "guestRating",
                    "primary": "Good 7+",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "35",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.35",
                      "referrerId": "HOT.SR.guestRating.35.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "guestRating.35",
                      "referrerId": "HOT.SR.guestRating.35.false:3"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionStackedTileField",
                "primary": "Star rating",
                "secondary": null,
                "tileMultiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "star",
                    "primary": "1",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "star",
                      "description": "star",
                      "size": null,
                      "token": "icon__star",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "10",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.10",
                      "referrerId": "HOT.SR.star.10.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.10",
                      "referrerId": "HOT.SR.star.10.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "star",
                    "primary": "2",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "star",
                      "description": "star",
                      "size": null,
                      "token": "icon__star",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "20",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.20",
                      "referrerId": "HOT.SR.star.20.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.20",
                      "referrerId": "HOT.SR.star.20.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "star",
                    "primary": "3",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "star",
                      "description": "star",
                      "size": null,
                      "token": "icon__star",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "30",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.30",
                      "referrerId": "HOT.SR.star.30.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.30",
                      "referrerId": "HOT.SR.star.30.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "star",
                    "primary": "4",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "star",
                      "description": "star",
                      "size": null,
                      "token": "icon__star",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "40",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.40",
                      "referrerId": "HOT.SR.star.40.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.40",
                      "referrerId": "HOT.SR.star.40.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "star",
                    "primary": "5",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "star",
                      "description": "star",
                      "size": null,
                      "token": "icon__star",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "50",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.50",
                      "referrerId": "HOT.SR.star.50.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "star.50",
                      "referrerId": "HOT.SR.star.50.false:4"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "Payment type",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 3,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "paymentType",
                    "primary": "Reserve now, pay later",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "PAY_LATER",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "paymentType.PAY_LATER",
                      "referrerId": "HOT.SR.paymentType.PAY_LATER.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "paymentType.PAY_LATER",
                      "referrerId": "HOT.SR.paymentType.PAY_LATER.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "paymentType",
                    "primary": "Pay with Hotels.com gift card",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "GIFT_CARD",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "paymentType.GIFT_CARD",
                      "referrerId": "HOT.SR.paymentType.GIFT_CARD.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "paymentType.GIFT_CARD",
                      "referrerId": "HOT.SR.paymentType.GIFT_CARD.false:1"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "Property type",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 3,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Vacation rentals",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "VACATION_RENTALS",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.VACATION_RENTALS",
                      "referrerId": "HOT.SR.lodging.VACATION_RENTALS.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.VACATION_RENTALS",
                      "referrerId": "HOT.SR.lodging.VACATION_RENTALS.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Hotel",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "HOTEL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.HOTEL",
                      "referrerId": "HOT.SR.lodging.HOTEL.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.HOTEL",
                      "referrerId": "HOT.SR.lodging.HOTEL.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Aparthotel",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "APART_HOTEL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.APART_HOTEL",
                      "referrerId": "HOT.SR.lodging.APART_HOTEL.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.APART_HOTEL",
                      "referrerId": "HOT.SR.lodging.APART_HOTEL.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Apartment",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "APARTMENT",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.APARTMENT",
                      "referrerId": "HOT.SR.lodging.APARTMENT.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.APARTMENT",
                      "referrerId": "HOT.SR.lodging.APARTMENT.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Bed & breakfast",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "BED_AND_BREAKFAST",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.BED_AND_BREAKFAST",
                      "referrerId": "HOT.SR.lodging.BED_AND_BREAKFAST.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.BED_AND_BREAKFAST",
                      "referrerId": "HOT.SR.lodging.BED_AND_BREAKFAST.false:4"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Private vacation home",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "VACATION_HOME",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.VACATION_HOME",
                      "referrerId": "HOT.SR.lodging.VACATION_HOME.true:5"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.VACATION_HOME",
                      "referrerId": "HOT.SR.lodging.VACATION_HOME.false:5"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Condo",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "CONDO",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.CONDO",
                      "referrerId": "HOT.SR.lodging.CONDO.true:6"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.CONDO",
                      "referrerId": "HOT.SR.lodging.CONDO.false:6"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "lodging",
                    "primary": "Motel",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "MOTEL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.MOTEL",
                      "referrerId": "HOT.SR.lodging.MOTEL.true:7"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "lodging.MOTEL",
                      "referrerId": "HOT.SR.lodging.MOTEL.false:7"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionStackedTileField",
                "primary": "Number of bedrooms",
                "secondary": null,
                "tileMultiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "bedroomFilter",
                    "primary": "Studio",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "0",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.0",
                      "referrerId": "HOT.SR.bedroomFilter.0.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.0",
                      "referrerId": "HOT.SR.bedroomFilter.0.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "bedroomFilter",
                    "primary": "1",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "1",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.1",
                      "referrerId": "HOT.SR.bedroomFilter.1.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.1",
                      "referrerId": "HOT.SR.bedroomFilter.1.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "bedroomFilter",
                    "primary": "2",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "2",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.2",
                      "referrerId": "HOT.SR.bedroomFilter.2.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.2",
                      "referrerId": "HOT.SR.bedroomFilter.2.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "bedroomFilter",
                    "primary": "3",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "3",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.3",
                      "referrerId": "HOT.SR.bedroomFilter.3.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.3",
                      "referrerId": "HOT.SR.bedroomFilter.3.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "bedroomFilter",
                    "primary": "4+",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "4",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.4",
                      "referrerId": "HOT.SR.bedroomFilter.4.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "bedroomFilter.4",
                      "referrerId": "HOT.SR.bedroomFilter.4.false:4"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingSelectionField",
                "primary": "Neighborhood",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 3,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "options": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Chicago",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "829",
                    "description": null,
                    "selected": true,
                    "disabled": false,
                    "default": true,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.829",
                      "referrerId": "HOT.SR.regionId.829.true:17"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.829",
                      "referrerId": "HOT.SR.regionId.829.false:17"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Chicago (and vicinity)",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "178248",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.178248",
                      "referrerId": "HOT.SR.regionId.178248.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.178248",
                      "referrerId": "HOT.SR.regionId.178248.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Downtown Chicago",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "6350699",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6350699",
                      "referrerId": "HOT.SR.regionId.6350699.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6350699",
                      "referrerId": "HOT.SR.regionId.6350699.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Magnificent Mile",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "800025",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.800025",
                      "referrerId": "HOT.SR.regionId.800025.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.800025",
                      "referrerId": "HOT.SR.regionId.800025.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "The Loop",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "800024",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.800024",
                      "referrerId": "HOT.SR.regionId.800024.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.800024",
                      "referrerId": "HOT.SR.regionId.800024.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "River North",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "6350695",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6350695",
                      "referrerId": "HOT.SR.regionId.6350695.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6350695",
                      "referrerId": "HOT.SR.regionId.6350695.false:4"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Oak Brook",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "9218",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9218",
                      "referrerId": "HOT.SR.regionId.9218.true:5"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9218",
                      "referrerId": "HOT.SR.regionId.9218.false:5"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Schaumburg",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "8107",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8107",
                      "referrerId": "HOT.SR.regionId.8107.true:6"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8107",
                      "referrerId": "HOT.SR.regionId.8107.false:6"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Chicago, IL (ORD-O'Hare Intl.)",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "4477519",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.4477519",
                      "referrerId": "HOT.SR.regionId.4477519.true:7"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.4477519",
                      "referrerId": "HOT.SR.regionId.4477519.false:7"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Skokie",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "6903",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6903",
                      "referrerId": "HOT.SR.regionId.6903.true:8"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6903",
                      "referrerId": "HOT.SR.regionId.6903.false:8"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Lombard",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "8393",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8393",
                      "referrerId": "HOT.SR.regionId.8393.true:9"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8393",
                      "referrerId": "HOT.SR.regionId.8393.false:9"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Naperville",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "9009",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9009",
                      "referrerId": "HOT.SR.regionId.9009.true:10"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9009",
                      "referrerId": "HOT.SR.regionId.9009.false:10"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Evanston",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "8049",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8049",
                      "referrerId": "HOT.SR.regionId.8049.true:11"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8049",
                      "referrerId": "HOT.SR.regionId.8049.false:11"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Tinley Park",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "55204",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.55204",
                      "referrerId": "HOT.SR.regionId.55204.true:12"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.55204",
                      "referrerId": "HOT.SR.regionId.55204.false:12"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Rosemont",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "7581",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.7581",
                      "referrerId": "HOT.SR.regionId.7581.true:13"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.7581",
                      "referrerId": "HOT.SR.regionId.7581.false:13"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "North Chicago",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "9157",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9157",
                      "referrerId": "HOT.SR.regionId.9157.true:14"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9157",
                      "referrerId": "HOT.SR.regionId.9157.false:14"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Oak Lawn Station",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "6213384",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6213384",
                      "referrerId": "HOT.SR.regionId.6213384.true:15"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6213384",
                      "referrerId": "HOT.SR.regionId.6213384.false:15"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Gurnee",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "8240",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8240",
                      "referrerId": "HOT.SR.regionId.8240.true:16"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.8240",
                      "referrerId": "HOT.SR.regionId.8240.false:16"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Aurora",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "6186",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6186",
                      "referrerId": "HOT.SR.regionId.6186.true:18"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.6186",
                      "referrerId": "HOT.SR.regionId.6186.false:18"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "regionId",
                    "primary": "Oakbrook Terrace",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "9064",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9064",
                      "referrerId": "HOT.SR.regionId.9064.true:19"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "regionId.9064",
                      "referrerId": "HOT.SR.regionId.9064.false:19"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingSelectionField",
                "primary": "Popular locations",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 3,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "options": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Any",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "",
                    "description": null,
                    "selected": true,
                    "disabled": false,
                    "default": true,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.ANY",
                      "referrerId": "HOT.SR.poi.ANY.true:19"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.ANY",
                      "referrerId": "HOT.SR.poi.ANY.false:19"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Grant Park",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.87325,-87.62055:507389",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.87325,-87.62055:507389",
                      "referrerId": "HOT.SR.poi.41.87325,-87.62055:507389.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.87325,-87.62055:507389",
                      "referrerId": "HOT.SR.poi.41.87325,-87.62055:507389.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "McCormick Place",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.85126,-87.61763:6069191",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.85126,-87.61763:6069191",
                      "referrerId": "HOT.SR.poi.41.85126,-87.61763:6069191.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.85126,-87.61763:6069191",
                      "referrerId": "HOT.SR.poi.41.85126,-87.61763:6069191.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Shedd Aquarium",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.86764,-87.61456:6065141",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.86764,-87.61456:6065141",
                      "referrerId": "HOT.SR.poi.41.86764,-87.61456:6065141.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.86764,-87.61456:6065141",
                      "referrerId": "HOT.SR.poi.41.86764,-87.61456:6065141.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Navy Pier",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.89172,-87.60445:6069215",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.89172,-87.60445:6069215",
                      "referrerId": "HOT.SR.poi.41.89172,-87.60445:6069215.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.89172,-87.60445:6069215",
                      "referrerId": "HOT.SR.poi.41.89172,-87.60445:6069215.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Millennium Park",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.88296,-87.62252:6069201",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.88296,-87.62252:6069201",
                      "referrerId": "HOT.SR.poi.41.88296,-87.62252:6069201.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.88296,-87.62252:6069201",
                      "referrerId": "HOT.SR.poi.41.88296,-87.62252:6069201.false:4"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Wrigley Field",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.94844,-87.65533:6034754",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.94844,-87.65533:6034754",
                      "referrerId": "HOT.SR.poi.41.94844,-87.65533:6034754.true:5"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.94844,-87.65533:6034754",
                      "referrerId": "HOT.SR.poi.41.94844,-87.65533:6034754.false:5"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Michigan Avenue",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.89171,-87.62417:6156167",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.89171,-87.62417:6156167",
                      "referrerId": "HOT.SR.poi.41.89171,-87.62417:6156167.true:6"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.89171,-87.62417:6156167",
                      "referrerId": "HOT.SR.poi.41.89171,-87.62417:6156167.false:6"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Willis Tower",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.87896,-87.63589:6064069",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.87896,-87.63589:6064069",
                      "referrerId": "HOT.SR.poi.41.87896,-87.63589:6064069.true:7"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.87896,-87.63589:6064069",
                      "referrerId": "HOT.SR.poi.41.87896,-87.63589:6064069.false:7"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "United Center",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.88071,-87.67418:6064077",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.88071,-87.67418:6064077",
                      "referrerId": "HOT.SR.poi.41.88071,-87.67418:6064077.true:8"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.88071,-87.67418:6064077",
                      "referrerId": "HOT.SR.poi.41.88071,-87.67418:6064077.false:8"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "University of Chicago",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.78959,-87.59946:6064081",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.78959,-87.59946:6064081",
                      "referrerId": "HOT.SR.poi.41.78959,-87.59946:6064081.true:9"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.78959,-87.59946:6064081",
                      "referrerId": "HOT.SR.poi.41.78959,-87.59946:6064081.false:9"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Donald E. Stephens Convention Center",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.97939,-87.86106:6034944",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.97939,-87.86106:6034944",
                      "referrerId": "HOT.SR.poi.41.97939,-87.86106:6034944.true:10"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.97939,-87.86106:6034944",
                      "referrerId": "HOT.SR.poi.41.97939,-87.86106:6034944.false:10"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Naval Base Great Lakes",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "42.30933,-87.84851:6069213",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.30933,-87.84851:6069213",
                      "referrerId": "HOT.SR.poi.42.30933,-87.84851:6069213.true:11"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.30933,-87.84851:6069213",
                      "referrerId": "HOT.SR.poi.42.30933,-87.84851:6069213.false:11"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Soldier Field",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.86234,-87.61669:6058043",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.86234,-87.61669:6058043",
                      "referrerId": "HOT.SR.poi.41.86234,-87.61669:6058043.true:12"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.86234,-87.61669:6058043",
                      "referrerId": "HOT.SR.poi.41.86234,-87.61669:6058043.false:12"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Chicago Water Tower",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.89702,-87.62422:6064051",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.89702,-87.62422:6064051",
                      "referrerId": "HOT.SR.poi.41.89702,-87.62422:6064051.true:13"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.89702,-87.62422:6064051",
                      "referrerId": "HOT.SR.poi.41.89702,-87.62422:6064051.false:13"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Chicago Theatre",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "41.88580,-87.62720:6064049",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.88580,-87.62720:6064049",
                      "referrerId": "HOT.SR.poi.41.88580,-87.62720:6064049.true:14"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.41.88580,-87.62720:6064049",
                      "referrerId": "HOT.SR.poi.41.88580,-87.62720:6064049.false:14"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Northwestern University",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "42.05235,-87.67872:6034942",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.05235,-87.67872:6034942",
                      "referrerId": "HOT.SR.poi.42.05235,-87.67872:6034942.true:15"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.05235,-87.67872:6034942",
                      "referrerId": "HOT.SR.poi.42.05235,-87.67872:6034942.false:15"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Loyola University Chicago",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "42.00044,-87.65974:6182907",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.00044,-87.65974:6182907",
                      "referrerId": "HOT.SR.poi.42.00044,-87.65974:6182907.true:16"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.00044,-87.65974:6182907",
                      "referrerId": "HOT.SR.poi.42.00044,-87.65974:6182907.false:16"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Six Flags Great America",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "42.36747,-87.93319:6023396",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.36747,-87.93319:6023396",
                      "referrerId": "HOT.SR.poi.42.36747,-87.93319:6023396.true:17"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.36747,-87.93319:6023396",
                      "referrerId": "HOT.SR.poi.42.36747,-87.93319:6023396.false:17"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "poi",
                    "primary": "Allstate Arena",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "42.00533,-87.88780:6069163",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.00533,-87.88780:6069163",
                      "referrerId": "HOT.SR.poi.42.00533,-87.88780:6069163.true:18"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "poi.42.00533,-87.88780:6069163",
                      "referrerId": "HOT.SR.poi.42.00533,-87.88780:6069163.false:18"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "Meal plans available",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 4,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "mealPlan",
                    "primary": "Breakfast included",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "FREE_BREAKFAST",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.FREE_BREAKFAST",
                      "referrerId": "HOT.SR.mealPlan.FREE_BREAKFAST.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.FREE_BREAKFAST",
                      "referrerId": "HOT.SR.mealPlan.FREE_BREAKFAST.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "mealPlan",
                    "primary": "Lunch included",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "HALF_BOARD",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.HALF_BOARD",
                      "referrerId": "HOT.SR.mealPlan.HALF_BOARD.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.HALF_BOARD",
                      "referrerId": "HOT.SR.mealPlan.HALF_BOARD.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "mealPlan",
                    "primary": "Dinner included",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "FULL_BOARD",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.FULL_BOARD",
                      "referrerId": "HOT.SR.mealPlan.FULL_BOARD.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.FULL_BOARD",
                      "referrerId": "HOT.SR.mealPlan.FULL_BOARD.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "mealPlan",
                    "primary": "All inclusive",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "ALL_INCLUSIVE",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.ALL_INCLUSIVE",
                      "referrerId": "HOT.SR.mealPlan.ALL_INCLUSIVE.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "mealPlan.ALL_INCLUSIVE",
                      "referrerId": "HOT.SR.mealPlan.ALL_INCLUSIVE.false:3"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionTileField",
                "primary": "Amenities",
                "secondary": null,
                "tileMultiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Pool",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "pool",
                      "description": "",
                      "size": null,
                      "token": "icon__pool",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "POOL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.POOL",
                      "referrerId": "HOT.SR.amenities.POOL.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.POOL",
                      "referrerId": "HOT.SR.amenities.POOL.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Kitchen",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "kitchen",
                      "description": "",
                      "size": null,
                      "token": "icon__kitchen",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "KITCHEN_KITCHENETTE",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.KITCHEN_KITCHENETTE",
                      "referrerId": "HOT.SR.amenities.KITCHEN_KITCHENETTE.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.KITCHEN_KITCHENETTE",
                      "referrerId": "HOT.SR.amenities.KITCHEN_KITCHENETTE.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Hot tub",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "hot_tub",
                      "description": "",
                      "size": null,
                      "token": "icon__hot_tub",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "HOT_TUB",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.HOT_TUB",
                      "referrerId": "HOT.SR.amenities.HOT_TUB.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.HOT_TUB",
                      "referrerId": "HOT.SR.amenities.HOT_TUB.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Pet friendly",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "pets",
                      "description": "",
                      "size": null,
                      "token": "icon__pets",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "PETS",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.PETS",
                      "referrerId": "HOT.SR.amenities.PETS.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.PETS",
                      "referrerId": "HOT.SR.amenities.PETS.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Wifi Included",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "wifi",
                      "description": "",
                      "size": null,
                      "token": "icon__wifi",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "WIFI",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.WIFI",
                      "referrerId": "HOT.SR.amenities.WIFI.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.WIFI",
                      "referrerId": "HOT.SR.amenities.WIFI.false:4"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Parking",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "local_parking",
                      "description": "",
                      "size": null,
                      "token": "icon__local_parking",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "FREE_PARKING",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.FREE_PARKING",
                      "referrerId": "HOT.SR.amenities.FREE_PARKING.true:5"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.FREE_PARKING",
                      "referrerId": "HOT.SR.amenities.FREE_PARKING.false:5"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Gym",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "fitness_center",
                      "description": "",
                      "size": null,
                      "token": "fitness_center",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "GYM",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.GYM",
                      "referrerId": "HOT.SR.amenities.GYM.true:6"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.GYM",
                      "referrerId": "HOT.SR.amenities.GYM.false:6"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Spa",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "spa",
                      "description": "",
                      "size": null,
                      "token": "icon__spa",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "SPA_ON_SITE",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.SPA_ON_SITE",
                      "referrerId": "HOT.SR.amenities.SPA_ON_SITE.true:7"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.SPA_ON_SITE",
                      "referrerId": "HOT.SR.amenities.SPA_ON_SITE.false:7"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Air conditioned",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "ac_unit",
                      "description": "",
                      "size": null,
                      "token": "icon__ac_unit",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "AIR_CONDITIONING",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.AIR_CONDITIONING",
                      "referrerId": "HOT.SR.amenities.AIR_CONDITIONING.true:8"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.AIR_CONDITIONING",
                      "referrerId": "HOT.SR.amenities.AIR_CONDITIONING.false:8"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Restaurant",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "local_dining",
                      "description": "",
                      "size": null,
                      "token": "local_dining",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "RESTAURANT_IN_HOTEL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.RESTAURANT_IN_HOTEL",
                      "referrerId": "HOT.SR.amenities.RESTAURANT_IN_HOTEL.true:9"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.RESTAURANT_IN_HOTEL",
                      "referrerId": "HOT.SR.amenities.RESTAURANT_IN_HOTEL.false:9"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Outdoor space",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "balcony",
                      "description": "",
                      "size": null,
                      "token": "balcony",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "BALCONY_OR_TERRACE",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.BALCONY_OR_TERRACE",
                      "referrerId": "HOT.SR.amenities.BALCONY_OR_TERRACE.true:10"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.BALCONY_OR_TERRACE",
                      "referrerId": "HOT.SR.amenities.BALCONY_OR_TERRACE.false:10"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Airport shuttle included",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "airport_shuttle",
                      "description": "",
                      "size": null,
                      "token": "icon__airport_shuttle",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "FREE_AIRPORT_TRANSPORTATION",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.FREE_AIRPORT_TRANSPORTATION",
                      "referrerId": "HOT.SR.amenities.FREE_AIRPORT_TRANSPORTATION.true:11"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.FREE_AIRPORT_TRANSPORTATION",
                      "referrerId": "HOT.SR.amenities.FREE_AIRPORT_TRANSPORTATION.false:11"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Cribs",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "bedding__crib",
                      "description": "",
                      "size": null,
                      "token": "bedding__crib",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "CRIB",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.CRIB",
                      "referrerId": "HOT.SR.amenities.CRIB.true:12"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.CRIB",
                      "referrerId": "HOT.SR.amenities.CRIB.false:12"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Washer and dryer",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "local_laundry_service",
                      "description": "",
                      "size": null,
                      "token": "icon__local_laundry_service",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "WASHER_DRYER",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.WASHER_DRYER",
                      "referrerId": "HOT.SR.amenities.WASHER_DRYER.true:13"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.WASHER_DRYER",
                      "referrerId": "HOT.SR.amenities.WASHER_DRYER.false:13"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Electric car charging station",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "ev_station",
                      "description": "",
                      "size": null,
                      "token": "ev_station",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "ELECTRIC_CAR",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.ELECTRIC_CAR",
                      "referrerId": "HOT.SR.amenities.ELECTRIC_CAR.true:14"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.ELECTRIC_CAR",
                      "referrerId": "HOT.SR.amenities.ELECTRIC_CAR.false:14"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Casino",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "casino",
                      "description": "",
                      "size": null,
                      "token": "icon__casino",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "CASINO",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.CASINO",
                      "referrerId": "HOT.SR.amenities.CASINO.true:15"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.CASINO",
                      "referrerId": "HOT.SR.amenities.CASINO.false:15"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Ocean view",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "water",
                      "description": "",
                      "size": null,
                      "token": "icon__water",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "OCEAN_VIEW",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.OCEAN_VIEW",
                      "referrerId": "HOT.SR.amenities.OCEAN_VIEW.true:16"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.OCEAN_VIEW",
                      "referrerId": "HOT.SR.amenities.OCEAN_VIEW.false:16"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "amenities",
                    "primary": "Water park",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "water_park",
                      "description": "",
                      "size": null,
                      "token": "water_park",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "WATER_PARK",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.WATER_PARK",
                      "referrerId": "HOT.SR.amenities.WATER_PARK.true:17"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "amenities.WATER_PARK",
                      "referrerId": "HOT.SR.amenities.WATER_PARK.false:17"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "One Key benefits",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 3,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "rewards",
                    "primary": "VIP Access properties",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "VIP",
                    "description": "Top-rated stays with member perks",
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "rewards.VIP",
                      "referrerId": "HOT.SR.rewards.VIP.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "rewards.VIP",
                      "referrerId": "HOT.SR.rewards.VIP.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "rewards",
                    "primary": "Member Prices",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "MEMBER_ONLY",
                    "description": "Instant savings of 10% or more on select stays",
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "rewards.MEMBER_ONLY",
                      "referrerId": "HOT.SR.rewards.MEMBER_ONLY.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "rewards.MEMBER_ONLY",
                      "referrerId": "HOT.SR.rewards.MEMBER_ONLY.false:1"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "Accessibility",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 3,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "Roll-in shower",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "ROLL_IN_SHOWER",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ROLL_IN_SHOWER",
                      "referrerId": "HOT.SR.accessibility.ROLL_IN_SHOWER.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ROLL_IN_SHOWER",
                      "referrerId": "HOT.SR.accessibility.ROLL_IN_SHOWER.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "Elevator",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "ELEVATOR",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ELEVATOR",
                      "referrerId": "HOT.SR.accessibility.ELEVATOR.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ELEVATOR",
                      "referrerId": "HOT.SR.accessibility.ELEVATOR.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "Stair-free path to entrance",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "STAIR_FREE_PATH",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.STAIR_FREE_PATH",
                      "referrerId": "HOT.SR.accessibility.STAIR_FREE_PATH.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.STAIR_FREE_PATH",
                      "referrerId": "HOT.SR.accessibility.STAIR_FREE_PATH.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "Wheelchair accessible parking",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "ACCESSIBLE_PARKING",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ACCESSIBLE_PARKING",
                      "referrerId": "HOT.SR.accessibility.ACCESSIBLE_PARKING.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ACCESSIBLE_PARKING",
                      "referrerId": "HOT.SR.accessibility.ACCESSIBLE_PARKING.false:3"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "Accessible bathroom",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "ACCESSIBLE_BATHROOM",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ACCESSIBLE_BATHROOM",
                      "referrerId": "HOT.SR.accessibility.ACCESSIBLE_BATHROOM.true:4"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.ACCESSIBLE_BATHROOM",
                      "referrerId": "HOT.SR.accessibility.ACCESSIBLE_BATHROOM.false:4"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "In-room accessibility",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "IN_ROOM_ACCESSIBLE",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.IN_ROOM_ACCESSIBLE",
                      "referrerId": "HOT.SR.accessibility.IN_ROOM_ACCESSIBLE.true:5"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.IN_ROOM_ACCESSIBLE",
                      "referrerId": "HOT.SR.accessibility.IN_ROOM_ACCESSIBLE.false:5"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "Service animals allowed",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "SERVICE_ANIMAL",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.SERVICE_ANIMAL",
                      "referrerId": "HOT.SR.accessibility.SERVICE_ANIMAL.true:6"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.SERVICE_ANIMAL",
                      "referrerId": "HOT.SR.accessibility.SERVICE_ANIMAL.false:6"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "accessibility",
                    "primary": "Sign language-capable staff",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "SIGN_LANGUAGE_INTERPRETER",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.SIGN_LANGUAGE_INTERPRETER",
                      "referrerId": "HOT.SR.accessibility.SIGN_LANGUAGE_INTERPRETER.true:7"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "accessibility.SIGN_LANGUAGE_INTERPRETER",
                      "referrerId": "HOT.SR.accessibility.SIGN_LANGUAGE_INTERPRETER.false:7"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "Traveler experience",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 4,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "travelerType",
                    "primary": "Eco-certified",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "ECO_CERTIFIED",
                    "description": "See properties certified by an accredited independent organization for meeting certain sustainability standards.",
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.ECO_CERTIFIED",
                      "referrerId": "HOT.SR.travelerType.ECO_CERTIFIED.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.ECO_CERTIFIED",
                      "referrerId": "HOT.SR.travelerType.ECO_CERTIFIED.false:0"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "travelerType",
                    "primary": "LGBTQ welcoming",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "LGBT",
                    "description": "See properties that pledge to make all guests feel safe, welcome, and respected.",
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.LGBT",
                      "referrerId": "HOT.SR.travelerType.LGBT.true:1"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.LGBT",
                      "referrerId": "HOT.SR.travelerType.LGBT.false:1"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "travelerType",
                    "primary": "Business friendly",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "BUSINESS",
                    "description": "See properties with amenities to help you work comfortably, like WiFi and breakfast.",
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.BUSINESS",
                      "referrerId": "HOT.SR.travelerType.BUSINESS.true:2"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.BUSINESS",
                      "referrerId": "HOT.SR.travelerType.BUSINESS.false:2"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "travelerType",
                    "primary": "Family friendly",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "FAMILY",
                    "description": "See properties that include family essentials like in-room conveniences and activities for the kids.",
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.FAMILY",
                      "referrerId": "HOT.SR.travelerType.FAMILY.true:3"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "travelerType.FAMILY",
                      "referrerId": "HOT.SR.travelerType.FAMILY.false:3"
                    }
                  }
                ]
              },
              {
                "__typename": "ShoppingMultiSelectionField",
                "primary": "Availability",
                "secondary": null,
                "expando": {
                  "__typename": "ShoppingSelectionExpando",
                  "threshold": 3,
                  "collapseLabel": "See less",
                  "expandLabel": "See more",
                  "collapseAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  },
                  "expandAnalytics": {
                    "__typename": "ClientSideAnalytics",
                    "linkName": "",
                    "referrerId": ""
                  }
                },
                "multiSelectionOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "availableFilter",
                    "primary": "Only show available properties",
                    "secondary": null,
                    "icon": {
                      "__typename": "Icon",
                      "id": "",
                      "description": "",
                      "size": null,
                      "token": "",
                      "theme": null
                    },
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "SHOW_AVAILABLE_ONLY",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "availableFilter.SHOW_AVAILABLE_ONLY",
                      "referrerId": "HOT.SR.availableFilter.SHOW_AVAILABLE_ONLY.true:0"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "availableFilter.SHOW_AVAILABLE_ONLY",
                      "referrerId": "HOT.SR.availableFilter.SHOW_AVAILABLE_ONLY.false:0"
                    }
                  }
                ]
              }
            ]
          }
        ],
        "sortSections": [
          {
            "__typename": "ShoppingSortAndFilterSection",
            "title": null,
            "fields": [
              {
                "__typename": "ShoppingDropdownField",
                "primary": "Sort by",
                "secondary": null,
                "dropdownFilterOptions": [
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "sort",
                    "primary": "Recommended",
                    "secondary": null,
                    "icon": null,
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "RECOMMENDED",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": true,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.RECOMMENDED",
                      "referrerId": "HOT.SR.sort.RECOMMENDED.true"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.RECOMMENDED",
                      "referrerId": "HOT.SR.sort.RECOMMENDED.false"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "sort",
                    "primary": "Price: low to high",
                    "secondary": null,
                    "icon": null,
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "PRICE_LOW_TO_HIGH",
                    "description": null,
                    "selected": true,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.PRICE_LOW_TO_HIGH",
                      "referrerId": "HOT.SR.sort.PRICE_LOW_TO_HIGH.true"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.PRICE_LOW_TO_HIGH",
                      "referrerId": "HOT.SR.sort.PRICE_LOW_TO_HIGH.false"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "sort",
                    "primary": "Price: high to low",
                    "secondary": null,
                    "icon": null,
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "PRICE_HIGH_TO_LOW",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.PRICE_HIGH_TO_LOW",
                      "referrerId": "HOT.SR.sort.PRICE_HIGH_TO_LOW.true"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.PRICE_HIGH_TO_LOW",
                      "referrerId": "HOT.SR.sort.PRICE_HIGH_TO_LOW.false"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "sort",
                    "primary": "Distance from downtown",
                    "secondary": null,
                    "icon": null,
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "DISTANCE",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.DISTANCE",
                      "referrerId": "HOT.SR.sort.DISTANCE.true"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.DISTANCE",
                      "referrerId": "HOT.SR.sort.DISTANCE.false"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "sort",
                    "primary": "Guest rating",
                    "secondary": null,
                    "icon": null,
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "REVIEW",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.REVIEW",
                      "referrerId": "HOT.SR.sort.REVIEW.true"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.REVIEW",
                      "referrerId": "HOT.SR.sort.REVIEW.false"
                    }
                  },
                  {
                    "__typename": "ShoppingSelectableFilterOption",
                    "id": "sort",
                    "primary": "Star rating",
                    "secondary": null,
                    "icon": null,
                    "analytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "",
                      "referrerId": ""
                    },
                    "value": "PROPERTY_CLASS",
                    "description": null,
                    "selected": false,
                    "disabled": false,
                    "default": false,
                    "selectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.PROPERTY_CLASS",
                      "referrerId": "HOT.SR.sort.PROPERTY_CLASS.true"
                    },
                    "deselectAnalytics": {
                      "__typename": "ClientSideAnalytics",
                      "linkName": "sort.PROPERTY_CLASS",
                      "referrerId": "HOT.SR.sort.PROPERTY_CLASS.false"
                    }
                  }
                ]
              }
            ]
          }
        ]
      },
      "properties": [
        {
          "__typename": "Property",
          "id": "11297",
          "featuredMessages": [],
          "name": "Best Western Chicago - Downers Grove",
          "availability": {
            "__typename": "PropertyAvailability",
            "available": true,
            "minRoomsLeft": 5
          },
          "propertyImage": {
            "__typename": "PropertyImage",
            "alt": "",
            "fallbackImage": null,
            "image": {
              "__typename": "Image",
              "description": "Lobby",
              "url": "https://images.trvl-media.com/lodging/1000000/20000/11300/11297/e68764ec.jpg?impolicy=resizecrop&rw=455&ra=fit"
            },
            "subjectId": 10001
          },
          "destinationInfo": {
            "__typename": "PropertyDestinationInfo",
            "distanceFromDestination": {
              "__typename": "Distance",
              "unit": "MILE",
              "value": 20.67
            },
            "distanceFromMessaging": "Downers Grove, 20.67 mi from Chicago",
            "regionId": "181500"
          },
          "legalDisclaimer": null,
          "listingFooter": null,
          "mapMarker": {
            "__typename": "MapMarker",
            "label": "$100",
            "latLong": {
              "__typename": "Coordinates",
              "latitude": 41.83256,
              "longitude": -88.02673
            }
          },
          "neighborhood": {
            "__typename": "Region",
            "name": "Downers Grove"
          },
          "offerBadge": {
            "__typename": "OfferBadge",
            "primary": {
              "__typename": "Badge",
              "text": "Great for families",
              "theme_temp": "FAMILY_FRIENDLY",
              "icon_temp": {
                "__typename": "Icon",
                "id": "family_friendly",
                "description": "family_friendly"
              },
              "mark": null
            },
            "secondary": {
              "__typename": "Badge",
              "text": "We have 5 left at",
              "theme_temp": "DEAL_GENERIC",
              "icon_temp": null,
              "mark": null
            }
          },
          "offerSummary": {
            "__typename": "OfferSummary",
            "messages": [
              {
                "__typename": "OfferSummaryMessage",
                "message": "Fully refundable",
                "theme": "SUCCESS",
                "type": "FREE_CANCEL",
                "mark": null
              },
              {
                "__typename": "OfferSummaryMessage",
                "message": "Reserve now, pay later",
                "theme": "SUCCESS",
                "type": "PAY_LATER",
                "mark": null
              }
            ],
            "attributes": [
              {
                "__typename": "OfferAttribute",
                "type": "FREE_CANCELLATION"
              },
              {
                "__typename": "OfferAttribute",
                "type": "PAYMENT_CHOICE"
              }
            ]
          },
          "pinnedDetails": null,
          "price": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$100"
              }
            ],
            "priceMessaging": null,
            "lead": {
              "__typename": "Money",
              "amount": 100.31,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$100"
            },
            "strikeOut": null,
            "displayMessages": [
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "DisplayPrice",
                    "disclaimer": null,
                    "price": {
                      "__typename": "FormattedMoney",
                      "formatted": "$100",
                      "accessibilityLabel": "The price is $100"
                    },
                    "role": "LEAD"
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_SECONDARY_PRICE",
                    "value": "$554 total",
                    "badge": null
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_TAX_AND_FEE_CLARIFY",
                    "value": "includes taxes & fees",
                    "badge": null
                  }
                ]
              }
            ],
            "strikeOutType": "STANDALONE",
            "priceMessages": [
              {
                "__typename": "LodgingPlainMessage",
                "value": "per night"
              },
              {
                "__typename": "LodgingPlainMessage",
                "value": "May 10 - May 15"
              }
            ]
          },
          "priceAfterLoyaltyPointsApplied": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$100"
              }
            ],
            "lead": {
              "__typename": "Money",
              "amount": 100.31,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$100"
            }
          },
          "propertyFees": [],
          "reviews": {
            "__typename": "PropertyReviewsSummary",
            "score": 8.6,
            "total": 1214
          },
          "sponsoredListing": null,
          "star": null,
          "supportingMessages": null,
          "regionId": "181500",
          "priceMetadata": {
            "__typename": "PropertyPriceMetadata",
            "discountType": null,
            "rateDiscount": null,
            "totalDiscountPercentage": null
          },
          "saveTripItem": {
            "__typename": "TripsSaveItem",
            "attributes": {
              "__typename": "TripsSaveStayAttributes",
              "checkInDate": {
                "__typename": "Date",
                "day": 10,
                "month": 5,
                "year": 2024
              },
              "checkoutDate": {
                "__typename": "Date",
                "day": 15,
                "month": 5,
                "year": 2024
              },
              "regionId": "829",
              "roomConfiguration": [
                {
                  "__typename": "PropertyRoom",
                  "childAges": [
                    5,
                    7
                  ],
                  "numberOfAdults": 2
                }
              ]
            },
            "initialChecked": false,
            "itemId": "11297",
            "remove": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Remove Best Western Chicago - Downers Grove from a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Remove",
                "referrerId": "HOT.SR.SaveTripItem-Remove"
              }
            },
            "save": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Save Best Western Chicago - Downers Grove to a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Save",
                "referrerId": "HOT.SR.SaveTripItem-Save"
              }
            },
            "source": "SEARCH_RESULTS"
          }
        },
        {
          "__typename": "Property",
          "id": "474236",
          "featuredMessages": [],
          "name": "Best Western Plus O'Hare International South Hotel",
          "availability": {
            "__typename": "PropertyAvailability",
            "available": true,
            "minRoomsLeft": 5
          },
          "propertyImage": {
            "__typename": "PropertyImage",
            "alt": "",
            "fallbackImage": null,
            "image": {
              "__typename": "Image",
              "description": "Exterior",
              "url": "https://images.trvl-media.com/lodging/1000000/480000/474300/474236/4e336a23.jpg?impolicy=resizecrop&rw=455&ra=fit"
            },
            "subjectId": 91024
          },
          "destinationInfo": {
            "__typename": "PropertyDestinationInfo",
            "distanceFromDestination": {
              "__typename": "Distance",
              "unit": "MILE",
              "value": 13.66
            },
            "distanceFromMessaging": "Franklin Park, 13.66 mi from Chicago",
            "regionId": "180646"
          },
          "legalDisclaimer": null,
          "listingFooter": null,
          "mapMarker": {
            "__typename": "MapMarker",
            "label": "$101",
            "latLong": {
              "__typename": "Coordinates",
              "latitude": 41.933563,
              "longitude": -87.88472
            }
          },
          "neighborhood": {
            "__typename": "Region",
            "name": "Franklin Park"
          },
          "offerBadge": {
            "__typename": "OfferBadge",
            "primary": {
              "__typename": "Badge",
              "text": "Great for families",
              "theme_temp": "FAMILY_FRIENDLY",
              "icon_temp": {
                "__typename": "Icon",
                "id": "family_friendly",
                "description": "family_friendly"
              },
              "mark": null
            },
            "secondary": {
              "__typename": "Badge",
              "text": "We have 5 left at",
              "theme_temp": "DEAL_GENERIC",
              "icon_temp": null,
              "mark": null
            }
          },
          "offerSummary": {
            "__typename": "OfferSummary",
            "messages": [],
            "attributes": []
          },
          "pinnedDetails": null,
          "price": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "priceMessaging": null,
            "lead": {
              "__typename": "Money",
              "amount": 100.804,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            },
            "strikeOut": null,
            "displayMessages": [
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "DisplayPrice",
                    "disclaimer": null,
                    "price": {
                      "__typename": "FormattedMoney",
                      "formatted": "$101",
                      "accessibilityLabel": "The price is $101"
                    },
                    "role": "LEAD"
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_SECONDARY_PRICE",
                    "value": "$577 total",
                    "badge": null
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_TAX_AND_FEE_CLARIFY",
                    "value": "includes taxes & fees",
                    "badge": null
                  }
                ]
              }
            ],
            "strikeOutType": "STANDALONE",
            "priceMessages": [
              {
                "__typename": "LodgingPlainMessage",
                "value": "per night"
              },
              {
                "__typename": "LodgingPlainMessage",
                "value": "May 10 - May 15"
              }
            ]
          },
          "priceAfterLoyaltyPointsApplied": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "lead": {
              "__typename": "Money",
              "amount": 100.804,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            }
          },
          "propertyFees": [],
          "reviews": {
            "__typename": "PropertyReviewsSummary",
            "score": 7.6,
            "total": 389
          },
          "sponsoredListing": null,
          "star": null,
          "supportingMessages": null,
          "regionId": "180646",
          "priceMetadata": {
            "__typename": "PropertyPriceMetadata",
            "discountType": null,
            "rateDiscount": null,
            "totalDiscountPercentage": null
          },
          "saveTripItem": {
            "__typename": "TripsSaveItem",
            "attributes": {
              "__typename": "TripsSaveStayAttributes",
              "checkInDate": {
                "__typename": "Date",
                "day": 10,
                "month": 5,
                "year": 2024
              },
              "checkoutDate": {
                "__typename": "Date",
                "day": 15,
                "month": 5,
                "year": 2024
              },
              "regionId": "829",
              "roomConfiguration": [
                {
                  "__typename": "PropertyRoom",
                  "childAges": [
                    5,
                    7
                  ],
                  "numberOfAdults": 2
                }
              ]
            },
            "initialChecked": false,
            "itemId": "474236",
            "remove": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Remove Best Western Plus O'Hare International South Hotel from a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Remove",
                "referrerId": "HOT.SR.SaveTripItem-Remove"
              }
            },
            "save": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Save Best Western Plus O'Hare International South Hotel to a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Save",
                "referrerId": "HOT.SR.SaveTripItem-Save"
              }
            },
            "source": "SEARCH_RESULTS"
          }
        },
        {
          "__typename": "Property",
          "id": "98901",
          "featuredMessages": [],
          "name": "Best Western Crossroads Inn",
          "availability": {
            "__typename": "PropertyAvailability",
            "available": true,
            "minRoomsLeft": null
          },
          "propertyImage": {
            "__typename": "PropertyImage",
            "alt": "",
            "fallbackImage": null,
            "image": {
              "__typename": "Image",
              "description": "Room",
              "url": "https://images.trvl-media.com/lodging/1000000/100000/99000/98901/f408ff4e.jpg?impolicy=resizecrop&rw=455&ra=fit"
            },
            "subjectId": 21001
          },
          "destinationInfo": {
            "__typename": "PropertyDestinationInfo",
            "distanceFromDestination": {
              "__typename": "Distance",
              "unit": "MILE",
              "value": 28.23
            },
            "distanceFromMessaging": "28.23 mi from Chicago",
            "regionId": "155703"
          },
          "legalDisclaimer": null,
          "listingFooter": null,
          "mapMarker": {
            "__typename": "MapMarker",
            "label": "$101",
            "latLong": {
              "__typename": "Coordinates",
              "latitude": 41.48738,
              "longitude": -87.469505
            }
          },
          "neighborhood": null,
          "offerBadge": null,
          "offerSummary": {
            "__typename": "OfferSummary",
            "messages": [
              {
                "__typename": "OfferSummaryMessage",
                "message": "Fully refundable",
                "theme": "SUCCESS",
                "type": "FREE_CANCEL",
                "mark": null
              },
              {
                "__typename": "OfferSummaryMessage",
                "message": "Reserve now, pay later",
                "theme": "SUCCESS",
                "type": "PAY_LATER",
                "mark": null
              }
            ],
            "attributes": [
              {
                "__typename": "OfferAttribute",
                "type": "FREE_CANCELLATION"
              },
              {
                "__typename": "OfferAttribute",
                "type": "PAYMENT_CHOICE"
              }
            ]
          },
          "pinnedDetails": null,
          "price": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "priceMessaging": null,
            "lead": {
              "__typename": "Money",
              "amount": 101.14,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            },
            "strikeOut": null,
            "displayMessages": [
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "DisplayPrice",
                    "disclaimer": null,
                    "price": {
                      "__typename": "FormattedMoney",
                      "formatted": "$101",
                      "accessibilityLabel": "The price is $101"
                    },
                    "role": "LEAD"
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_SECONDARY_PRICE",
                    "value": "$574 total",
                    "badge": null
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_TAX_AND_FEE_CLARIFY",
                    "value": "includes taxes & fees",
                    "badge": null
                  }
                ]
              }
            ],
            "strikeOutType": "STANDALONE",
            "priceMessages": [
              {
                "__typename": "LodgingPlainMessage",
                "value": "per night"
              },
              {
                "__typename": "LodgingPlainMessage",
                "value": "May 10 - May 15"
              }
            ]
          },
          "priceAfterLoyaltyPointsApplied": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "lead": {
              "__typename": "Money",
              "amount": 101.14,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            }
          },
          "propertyFees": [
            {
              "__typename": "Fees",
              "type": "RESORT"
            }
          ],
          "reviews": {
            "__typename": "PropertyReviewsSummary",
            "score": 7.2,
            "total": 718
          },
          "sponsoredListing": null,
          "star": null,
          "supportingMessages": null,
          "regionId": "155703",
          "priceMetadata": {
            "__typename": "PropertyPriceMetadata",
            "discountType": null,
            "rateDiscount": null,
            "totalDiscountPercentage": null
          },
          "saveTripItem": {
            "__typename": "TripsSaveItem",
            "attributes": {
              "__typename": "TripsSaveStayAttributes",
              "checkInDate": {
                "__typename": "Date",
                "day": 10,
                "month": 5,
                "year": 2024
              },
              "checkoutDate": {
                "__typename": "Date",
                "day": 15,
                "month": 5,
                "year": 2024
              },
              "regionId": "829",
              "roomConfiguration": [
                {
                  "__typename": "PropertyRoom",
                  "childAges": [
                    5,
                    7
                  ],
                  "numberOfAdults": 2
                }
              ]
            },
            "initialChecked": false,
            "itemId": "98901",
            "remove": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Remove Best Western Crossroads Inn from a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Remove",
                "referrerId": "HOT.SR.SaveTripItem-Remove"
              }
            },
            "save": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Save Best Western Crossroads Inn to a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Save",
                "referrerId": "HOT.SR.SaveTripItem-Save"
              }
            },
            "source": "SEARCH_RESULTS"
          }
        }
      ],
      "propertySearchListings": [
        {
          "__typename": "LodgingCard"
        },
        {
          "__typename": "LodgingCard"
        },
        {
          "__typename": "LodgingCard"
        },
        {
          "__typename": "SponsoredContentPlacement"
        },
        {
          "__typename": "Property",
          "id": "11297",
          "featuredMessages": [],
          "name": "Best Western Chicago - Downers Grove",
          "availability": {
            "__typename": "PropertyAvailability",
            "available": true,
            "minRoomsLeft": 5
          },
          "propertyImage": {
            "__typename": "PropertyImage",
            "alt": "",
            "fallbackImage": null,
            "image": {
              "__typename": "Image",
              "description": "Lobby",
              "url": "https://images.trvl-media.com/lodging/1000000/20000/11300/11297/e68764ec.jpg?impolicy=resizecrop&rw=455&ra=fit"
            },
            "subjectId": 10001
          },
          "destinationInfo": {
            "__typename": "PropertyDestinationInfo",
            "distanceFromDestination": {
              "__typename": "Distance",
              "unit": "MILE",
              "value": 20.67
            },
            "distanceFromMessaging": "Downers Grove, 20.67 mi from Chicago",
            "regionId": "181500"
          },
          "legalDisclaimer": null,
          "listingFooter": null,
          "mapMarker": {
            "__typename": "MapMarker",
            "label": "$100",
            "latLong": {
              "__typename": "Coordinates",
              "latitude": 41.83256,
              "longitude": -88.02673
            }
          },
          "neighborhood": {
            "__typename": "Region",
            "name": "Downers Grove"
          },
          "offerBadge": {
            "__typename": "OfferBadge",
            "primary": {
              "__typename": "Badge",
              "text": "Great for families",
              "theme_temp": "FAMILY_FRIENDLY",
              "icon_temp": {
                "__typename": "Icon",
                "id": "family_friendly",
                "description": "family_friendly"
              },
              "mark": null
            },
            "secondary": {
              "__typename": "Badge",
              "text": "We have 5 left at",
              "theme_temp": "DEAL_GENERIC",
              "icon_temp": null,
              "mark": null
            }
          },
          "offerSummary": {
            "__typename": "OfferSummary",
            "messages": [
              {
                "__typename": "OfferSummaryMessage",
                "message": "Fully refundable",
                "theme": "SUCCESS",
                "type": "FREE_CANCEL",
                "mark": null
              },
              {
                "__typename": "OfferSummaryMessage",
                "message": "Reserve now, pay later",
                "theme": "SUCCESS",
                "type": "PAY_LATER",
                "mark": null
              }
            ],
            "attributes": [
              {
                "__typename": "OfferAttribute",
                "type": "FREE_CANCELLATION"
              },
              {
                "__typename": "OfferAttribute",
                "type": "PAYMENT_CHOICE"
              }
            ]
          },
          "pinnedDetails": null,
          "price": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$100"
              }
            ],
            "priceMessaging": null,
            "lead": {
              "__typename": "Money",
              "amount": 100.31,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$100"
            },
            "strikeOut": null,
            "displayMessages": [
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "DisplayPrice",
                    "disclaimer": null,
                    "price": {
                      "__typename": "FormattedMoney",
                      "formatted": "$100",
                      "accessibilityLabel": "The price is $100"
                    },
                    "role": "LEAD"
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_SECONDARY_PRICE",
                    "value": "$554 total",
                    "badge": null
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_TAX_AND_FEE_CLARIFY",
                    "value": "includes taxes & fees",
                    "badge": null
                  }
                ]
              }
            ],
            "strikeOutType": "STANDALONE",
            "priceMessages": [
              {
                "__typename": "LodgingPlainMessage",
                "value": "per night"
              },
              {
                "__typename": "LodgingPlainMessage",
                "value": "May 10 - May 15"
              }
            ]
          },
          "priceAfterLoyaltyPointsApplied": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$100"
              }
            ],
            "lead": {
              "__typename": "Money",
              "amount": 100.31,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$100"
            }
          },
          "propertyFees": [],
          "reviews": {
            "__typename": "PropertyReviewsSummary",
            "score": 8.6,
            "total": 1214
          },
          "sponsoredListing": null,
          "star": null,
          "supportingMessages": null,
          "regionId": "181500",
          "priceMetadata": {
            "__typename": "PropertyPriceMetadata",
            "discountType": null,
            "rateDiscount": null,
            "totalDiscountPercentage": null
          },
          "saveTripItem": {
            "__typename": "TripsSaveItem",
            "attributes": {
              "__typename": "TripsSaveStayAttributes",
              "checkInDate": {
                "__typename": "Date",
                "day": 10,
                "month": 5,
                "year": 2024
              },
              "checkoutDate": {
                "__typename": "Date",
                "day": 15,
                "month": 5,
                "year": 2024
              },
              "regionId": "829",
              "roomConfiguration": [
                {
                  "__typename": "PropertyRoom",
                  "childAges": [
                    5,
                    7
                  ],
                  "numberOfAdults": 2
                }
              ]
            },
            "initialChecked": false,
            "itemId": "11297",
            "remove": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Remove Best Western Chicago - Downers Grove from a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Remove",
                "referrerId": "HOT.SR.SaveTripItem-Remove"
              }
            },
            "save": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Save Best Western Chicago - Downers Grove to a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Save",
                "referrerId": "HOT.SR.SaveTripItem-Save"
              }
            },
            "source": "SEARCH_RESULTS"
          }
        },
        {
          "__typename": "Property",
          "id": "474236",
          "featuredMessages": [],
          "name": "Best Western Plus O'Hare International South Hotel",
          "availability": {
            "__typename": "PropertyAvailability",
            "available": true,
            "minRoomsLeft": 5
          },
          "propertyImage": {
            "__typename": "PropertyImage",
            "alt": "",
            "fallbackImage": null,
            "image": {
              "__typename": "Image",
              "description": "Exterior",
              "url": "https://images.trvl-media.com/lodging/1000000/480000/474300/474236/4e336a23.jpg?impolicy=resizecrop&rw=455&ra=fit"
            },
            "subjectId": 91024
          },
          "destinationInfo": {
            "__typename": "PropertyDestinationInfo",
            "distanceFromDestination": {
              "__typename": "Distance",
              "unit": "MILE",
              "value": 13.66
            },
            "distanceFromMessaging": "Franklin Park, 13.66 mi from Chicago",
            "regionId": "180646"
          },
          "legalDisclaimer": null,
          "listingFooter": null,
          "mapMarker": {
            "__typename": "MapMarker",
            "label": "$101",
            "latLong": {
              "__typename": "Coordinates",
              "latitude": 41.933563,
              "longitude": -87.88472
            }
          },
          "neighborhood": {
            "__typename": "Region",
            "name": "Franklin Park"
          },
          "offerBadge": {
            "__typename": "OfferBadge",
            "primary": {
              "__typename": "Badge",
              "text": "Great for families",
              "theme_temp": "FAMILY_FRIENDLY",
              "icon_temp": {
                "__typename": "Icon",
                "id": "family_friendly",
                "description": "family_friendly"
              },
              "mark": null
            },
            "secondary": {
              "__typename": "Badge",
              "text": "We have 5 left at",
              "theme_temp": "DEAL_GENERIC",
              "icon_temp": null,
              "mark": null
            }
          },
          "offerSummary": {
            "__typename": "OfferSummary",
            "messages": [],
            "attributes": []
          },
          "pinnedDetails": null,
          "price": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "priceMessaging": null,
            "lead": {
              "__typename": "Money",
              "amount": 100.804,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            },
            "strikeOut": null,
            "displayMessages": [
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "DisplayPrice",
                    "disclaimer": null,
                    "price": {
                      "__typename": "FormattedMoney",
                      "formatted": "$101",
                      "accessibilityLabel": "The price is $101"
                    },
                    "role": "LEAD"
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_SECONDARY_PRICE",
                    "value": "$577 total",
                    "badge": null
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_TAX_AND_FEE_CLARIFY",
                    "value": "includes taxes & fees",
                    "badge": null
                  }
                ]
              }
            ],
            "strikeOutType": "STANDALONE",
            "priceMessages": [
              {
                "__typename": "LodgingPlainMessage",
                "value": "per night"
              },
              {
                "__typename": "LodgingPlainMessage",
                "value": "May 10 - May 15"
              }
            ]
          },
          "priceAfterLoyaltyPointsApplied": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "lead": {
              "__typename": "Money",
              "amount": 100.804,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            }
          },
          "propertyFees": [],
          "reviews": {
            "__typename": "PropertyReviewsSummary",
            "score": 7.6,
            "total": 389
          },
          "sponsoredListing": null,
          "star": null,
          "supportingMessages": null,
          "regionId": "180646",
          "priceMetadata": {
            "__typename": "PropertyPriceMetadata",
            "discountType": null,
            "rateDiscount": null,
            "totalDiscountPercentage": null
          },
          "saveTripItem": {
            "__typename": "TripsSaveItem",
            "attributes": {
              "__typename": "TripsSaveStayAttributes",
              "checkInDate": {
                "__typename": "Date",
                "day": 10,
                "month": 5,
                "year": 2024
              },
              "checkoutDate": {
                "__typename": "Date",
                "day": 15,
                "month": 5,
                "year": 2024
              },
              "regionId": "829",
              "roomConfiguration": [
                {
                  "__typename": "PropertyRoom",
                  "childAges": [
                    5,
                    7
                  ],
                  "numberOfAdults": 2
                }
              ]
            },
            "initialChecked": false,
            "itemId": "474236",
            "remove": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Remove Best Western Plus O'Hare International South Hotel from a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Remove",
                "referrerId": "HOT.SR.SaveTripItem-Remove"
              }
            },
            "save": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Save Best Western Plus O'Hare International South Hotel to a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Save",
                "referrerId": "HOT.SR.SaveTripItem-Save"
              }
            },
            "source": "SEARCH_RESULTS"
          }
        },
        {
          "__typename": "Property",
          "id": "98901",
          "featuredMessages": [],
          "name": "Best Western Crossroads Inn",
          "availability": {
            "__typename": "PropertyAvailability",
            "available": true,
            "minRoomsLeft": null
          },
          "propertyImage": {
            "__typename": "PropertyImage",
            "alt": "",
            "fallbackImage": null,
            "image": {
              "__typename": "Image",
              "description": "Room",
              "url": "https://images.trvl-media.com/lodging/1000000/100000/99000/98901/f408ff4e.jpg?impolicy=resizecrop&rw=455&ra=fit"
            },
            "subjectId": 21001
          },
          "destinationInfo": {
            "__typename": "PropertyDestinationInfo",
            "distanceFromDestination": {
              "__typename": "Distance",
              "unit": "MILE",
              "value": 28.23
            },
            "distanceFromMessaging": "28.23 mi from Chicago",
            "regionId": "155703"
          },
          "legalDisclaimer": null,
          "listingFooter": null,
          "mapMarker": {
            "__typename": "MapMarker",
            "label": "$101",
            "latLong": {
              "__typename": "Coordinates",
              "latitude": 41.48738,
              "longitude": -87.469505
            }
          },
          "neighborhood": null,
          "offerBadge": null,
          "offerSummary": {
            "__typename": "OfferSummary",
            "messages": [
              {
                "__typename": "OfferSummaryMessage",
                "message": "Fully refundable",
                "theme": "SUCCESS",
                "type": "FREE_CANCEL",
                "mark": null
              },
              {
                "__typename": "OfferSummaryMessage",
                "message": "Reserve now, pay later",
                "theme": "SUCCESS",
                "type": "PAY_LATER",
                "mark": null
              }
            ],
            "attributes": [
              {
                "__typename": "OfferAttribute",
                "type": "FREE_CANCELLATION"
              },
              {
                "__typename": "OfferAttribute",
                "type": "PAYMENT_CHOICE"
              }
            ]
          },
          "pinnedDetails": null,
          "price": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "priceMessaging": null,
            "lead": {
              "__typename": "Money",
              "amount": 101.14,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            },
            "strikeOut": null,
            "displayMessages": [
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "DisplayPrice",
                    "disclaimer": null,
                    "price": {
                      "__typename": "FormattedMoney",
                      "formatted": "$101",
                      "accessibilityLabel": "The price is $101"
                    },
                    "role": "LEAD"
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_SECONDARY_PRICE",
                    "value": "$574 total",
                    "badge": null
                  }
                ]
              },
              {
                "__typename": "PriceDisplayMessage",
                "lineItems": [
                  {
                    "__typename": "LodgingEnrichedMessage",
                    "accessibilityLabel": null,
                    "mark": null,
                    "state": "BREAKOUT_TYPE_TAX_AND_FEE_CLARIFY",
                    "value": "includes taxes & fees",
                    "badge": null
                  }
                ]
              }
            ],
            "strikeOutType": "STANDALONE",
            "priceMessages": [
              {
                "__typename": "LodgingPlainMessage",
                "value": "per night"
              },
              {
                "__typename": "LodgingPlainMessage",
                "value": "May 10 - May 15"
              }
            ]
          },
          "priceAfterLoyaltyPointsApplied": {
            "__typename": "PropertyPrice",
            "options": [
              {
                "__typename": "PropertyPriceOption",
                "strikeOut": null,
                "disclaimer": null,
                "formattedDisplayPrice": "$101"
              }
            ],
            "lead": {
              "__typename": "Money",
              "amount": 101.14,
              "currencyInfo": {
                "__typename": "Currency",
                "code": "USD",
                "symbol": "$"
              },
              "formatted": "$101"
            }
          },
          "propertyFees": [
            {
              "__typename": "Fees",
              "type": "RESORT"
            }
          ],
          "reviews": {
            "__typename": "PropertyReviewsSummary",
            "score": 7.2,
            "total": 718
          },
          "sponsoredListing": null,
          "star": null,
          "supportingMessages": null,
          "regionId": "155703",
          "priceMetadata": {
            "__typename": "PropertyPriceMetadata",
            "discountType": null,
            "rateDiscount": null,
            "totalDiscountPercentage": null
          },
          "saveTripItem": {
            "__typename": "TripsSaveItem",
            "attributes": {
              "__typename": "TripsSaveStayAttributes",
              "checkInDate": {
                "__typename": "Date",
                "day": 10,
                "month": 5,
                "year": 2024
              },
              "checkoutDate": {
                "__typename": "Date",
                "day": 15,
                "month": 5,
                "year": 2024
              },
              "regionId": "829",
              "roomConfiguration": [
                {
                  "__typename": "PropertyRoom",
                  "childAges": [
                    5,
                    7
                  ],
                  "numberOfAdults": 2
                }
              ]
            },
            "initialChecked": false,
            "itemId": "98901",
            "remove": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Remove Best Western Crossroads Inn from a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Remove",
                "referrerId": "HOT.SR.SaveTripItem-Remove"
              }
            },
            "save": {
              "__typename": "TripsSaveItemProperties",
              "accessibility": "Save Best Western Crossroads Inn to a trip",
              "analytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "SaveTripItem-Save",
                "referrerId": "HOT.SR.SaveTripItem-Save"
              }
            },
            "source": "SEARCH_RESULTS"
          }
        }
      ],
      "summary": {
        "__typename": "PropertyResultsSummary",
        "matchedPropertiesSize": 651,
        "pricingScheme": {
          "__typename": "PricingScheme",
          "type": "DAILY_RATE"
        },
        "regionCompression": null,
        "loyaltyInfo": {
          "__typename": "PropertyLoyaltyDiscount",
          "saveWithPointsMessage": null,
          "saveWithPointsActionMessage": null
        },
        "resultsTitleModel": {
          "__typename": "ResultTitleModel",
          "header": "651 properties"
        },
        "resultsSummary": [
          {
            "__typename": "LodgingPlainMessage"
          },
          {
            "__typename": "LodgingLinkMessage",
            "accessibilityLabel": "Opens in a new window",
            "value": "What we are paid impacts our sort order",
            "link": {
              "__typename": "LodgingLink",
              "clientSideAnalytics": {
                "__typename": "ClientSideAnalytics",
                "linkName": "Sort disclaimer",
                "referrerId": "HOT.HSR.RecommendedSort.FAQlink"
              },
              "uri": {
                "__typename": "HttpURI",
                "value": "https://service.hotels.com/en-us/#/article/19645"
              }
            }
          }
        ]
      },
      "searchCriteria": {
        "__typename": "SearchCriteria",
        "resolvedDateRange": null
      },
      "shoppingContext": {
        "__typename": "ShoppingContext",
        "multiItem": null
      },
      "map": {
        "__typename": "PropertySearchMap",
        "subtitle": null
      },
      "clickstream": {
        "__typename": "SearchClickstreamEvents",
        "searchResultsViewed": null
      }
    }
  }
}

```
