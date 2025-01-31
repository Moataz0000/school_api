from .models import Subject

class ManageSubject:
    """This is a layer between the database and serializer to manage the Subject model"""

    @staticmethod
    def get_subject_by_id(pk):
        """Retrieve a subject by ID or return None if not found."""
        return Subject.objects.filter(id=pk).first()  

    @staticmethod
    def get_all_available_subjects():
        """Retrieve all active subjects."""
        return Subject.objects.filter(is_active=True)

    @staticmethod
    def add_subject(title: str, is_active: bool = True):
        """Add a new subject."""
        return Subject.objects.create(title=title, is_active=is_active)

    @staticmethod
    def modify_subject(pk: int, title: str, is_active: bool):
        """Modify an existing subject."""
        subject = ManageSubject.get_subject_by_id(pk)
        if subject:
            subject.title = title
            subject.is_active = is_active
            subject.save()
            return subject
        return None  # Return None if subject does not exist

    @staticmethod
    def delete_subject(pk: int):
        """Delete a subject by ID and return True if deleted, False otherwise."""
        subject = ManageSubject.get_subject_by_id(pk)
        if subject:
            subject.delete()
            return True
        return False  # Return False instead of None for clarity
