from src.models import Accommodation, Notification, SearchResults
import logging

logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)
logger = logging.getLogger("accommodation_notifier")


class NotificationBuilder:
    """Class that builds notifications from search results."""

    def __init__(self, notify_when_no_results: bool = False):
        self.notify_when_no_results = notify_when_no_results

    def search_results_notification(
        self, search_results: SearchResults
    ) -> Notification | None:
        
        logging.info("sending notification - ")
        accommodations = search_results.accommodations
        if not accommodations and not self.notify_when_no_results:
            logging.info("not available")
            return Notification(message="not available")

        if not accommodations:
            message = "Aucun logement trouvé. Voici une liste des ponts de France où vous pourriez dormir : https://fr.wikipedia.org/wiki/Liste_de_ponts_de_France"
        else:
            s = "s" if len(accommodations) > 1 else ""
            verb = "sont" if len(accommodations) > 1 else "est"
            message = f"Bonne nouvelle 😯, {len(accommodations)} logement{s} {verb} disponible{s} : \n "
	
	
        def format_one_accommodation(accommodation: Accommodation):
            price = (
                f"{accommodation.price}€"
                if isinstance(accommodation.price, float)
                else accommodation.price
            )

            link = f"https://trouverunlogement.lescrous.fr/tools/36/accommodations/{accommodation.id}"

            return f"[*{accommodation.title}*]({link}) ({price})"

        message += "\n\n".join(map(format_one_accommodation, accommodations))

        message += f"\n\n{search_results.search_url}"

        logging.info("sending notification")
        return Notification(message=message)

